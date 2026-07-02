#!/usr/bin/env python3
"""Render a completed visual_plan.json into Markdown and prompt files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


PRESETS: dict[str, dict[str, Any]] = {
    "xiaohongshu": {"width": 1242, "height": 1660, "aspect_ratio": "3:4", "page_count": 6},
    "square": {"width": 1080, "height": 1080, "aspect_ratio": "1:1", "page_count": 1},
    "portrait-social": {"width": 1080, "height": 1350, "aspect_ratio": "4:5", "page_count": 4},
    "wide-hero": {"width": 1920, "height": 1080, "aspect_ratio": "16:9", "page_count": 1},
    "ppt-slide": {"width": 1920, "height": 1080, "aspect_ratio": "16:9", "page_count": 1},
}

DEFAULT_STYLE_SYSTEM = (
    "研究档案式编辑设计。纸白和冷灰为底，理性蓝结构线，克制黑色标题，"
    "真实工作材料，证据层次，轻微颗粒质感，只在帮助理解时加入少量手写批注、"
    "圈画、对号/叉号或签字笔痕迹。画面先结构后装饰，少字，高层级，"
    "避免通用AI海报感、蓝紫渐变科技风、3D图标堆和PPT卡片感。"
)

DEFAULT_COLOR_MATERIALS = "纸白、冷灰、理性蓝结构线、克制黑色标题、少量红色批注、轻微颗粒质感"

DEFAULT_NEGATIVES = [
    "机器人主角",
    "AI 大脑",
    "赛博城市",
    "随机 3D 图标堆",
    "蓝紫渐变 SaaS 模板",
    "PPT 卡片堆",
    "随机 Logo",
    "水印",
    "满屏小字",
]

AI_MEDICAL_ADDON = (
    "AI+医学模式：表现为可追责的临床协作系统。"
    "画面中有医生、报告、病历、影像或随访材料作为真实语境。"
    "AI 只作为辅助分析层，不是最终决策者。"
    "医生确认、审核状态、责任链和随访闭环必须可见。"
    "病历和报告不能出现可识别个人信息。"
    "避免机器人医生、AI 大脑、赛博医院、神奇诊断和 AI 自主治疗暗示。"
)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError("visual_plan.json 必须是一个 JSON 对象")
    return data


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str):
        return [line.strip() for line in value.splitlines() if line.strip()]
    return [str(value)]


def pick_dimensions(plan: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    preset_name = args.preset or plan.get("platform") or "xiaohongshu"
    preset = PRESETS.get(str(preset_name), PRESETS["xiaohongshu"]).copy()

    if args.preset:
        dimensions = {"platform": preset_name, **preset}
    else:
        dimensions = {
            "platform": preset_name,
            "width": plan.get("width", preset["width"]),
            "height": plan.get("height", preset["height"]),
            "aspect_ratio": plan.get("aspect_ratio", preset["aspect_ratio"]),
            "page_count": plan.get("page_count", preset["page_count"]),
        }

    if args.width:
        dimensions["width"] = args.width
    if args.height:
        dimensions["height"] = args.height
    if args.aspect_ratio:
        dimensions["aspect_ratio"] = args.aspect_ratio
    if args.page_count:
        dimensions["page_count"] = args.page_count

    return dimensions


def normalize_plan(plan: dict[str, Any], dimensions: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(plan)
    normalized.update(dimensions)
    normalized["aesthetic_style"] = normalized.get("aesthetic_style") or "研究档案式"
    normalized["style_system"] = normalized.get("style_system") or DEFAULT_STYLE_SYSTEM

    pages = normalized.get("pages")
    if not isinstance(pages, list) or not pages:
        raise ValueError("visual_plan.json 必须包含非空的 pages 数组")

    page_count = int(dimensions["page_count"])
    normalized["page_count"] = page_count
    normalized["pages"] = pages[:page_count]

    for index, page in enumerate(normalized["pages"], start=1):
        if not isinstance(page, dict):
            raise ValueError("每个 page 都必须是 JSON 对象")
        page.setdefault("page", f"{index:02d}/{page_count:02d}")
        page.setdefault("title", f"第 {index} 页")
        page.setdefault("body_text", "")
        page.setdefault("visual_focus", normalized.get("protagonist", "核心证据"))
        page.setdefault("real_scene", "与主题相关的真实材料，以证据方式排列")
        page.setdefault("diagram_flow", "一条简单的证据链或责任路径")
        page.setdefault("text_layer", page.get("title", ""))
        page.setdefault("color_materials", normalized.get("color_materials", DEFAULT_COLOR_MATERIALS))
        page["negative_prompts"] = as_list(page.get("negative_prompts")) or as_list(normalized.get("negative_prompts")) or DEFAULT_NEGATIVES

    normalized["negative_prompts"] = as_list(normalized.get("negative_prompts")) or DEFAULT_NEGATIVES
    normalized["quality_checklist"] = as_list(normalized.get("quality_checklist")) or [
        "视觉命题清楚",
        "缩小到预览尺寸时主角仍然明确",
        "每页只讲一个意思",
        "已经完成 30% 删除实验",
        "没有残留廉价 AI 视觉套路",
    ]
    return normalized


def is_ai_medical(plan: dict[str, Any]) -> bool:
    haystack = " ".join(
        str(plan.get(key, ""))
        for key in ["domain", "topic", "core_claim", "visual_thesis", "protagonist"]
    ).lower()
    return any(token in haystack for token in ["medical", "medicine", "health", "clinical", "医学", "医疗", "医生", "患者", "病历", "影像"])


def format_negative(items: list[str]) -> str:
    return "; ".join(items)


def platform_guidance(plan: dict[str, Any]) -> str:
    if str(plan.get("platform", "")) != "ppt-slide":
        return ""
    return (
        "\nPPT 演示页要求：适合 16:9 投影观看，四周保留安全边距，"
        "大标题远距离可读，主视觉占据中央主要区域，辅助文字不超过两句，"
        "流程节点控制在 3-5 个，整体少字、高对比、强层级。"
        "避免企业汇报 PPT 感、复杂表格、密集小字和装饰性卡片堆。\n"
    )


def render_page_prompt(plan: dict[str, Any], page: dict[str, Any]) -> str:
    negative_prompts = format_negative(as_list(page.get("negative_prompts")) or as_list(plan.get("negative_prompts")))
    if int(plan.get("page_count", 1)) == 1:
        base = f"""编辑设计视觉图，比例 {plan["aspect_ratio"]}，尺寸 {plan["width"]}x{plan["height"]}。

核心判断：{plan.get("core_claim", "")}
视觉命题：{plan.get("visual_thesis", "")}
主角：{plan.get("protagonist", "")}
视觉态度：{plan.get("visual_attitude", "")}

画面用一个清楚的中心场景组织信息：真实材料第一层，图解/证据叠加第二层，短句观点第三层。缩小到预览尺寸时仍能看懂。

画面文字：
标题：“{page.get("title", "")}”
辅助：“{page.get("body_text", "")}”

风格与材质：
{plan.get("style_system", "")}
{page.get("color_materials", "")}

避免出现：
{negative_prompts}
"""
    else:
        base = f"""知识卡片单页，比例 {plan["aspect_ratio"]}，尺寸 {plan["width"]}x{plan["height"]}，第 {page["page"]} 页。

视觉命题：{plan.get("visual_thesis", "")}
主角：{plan.get("protagonist", "")}
视觉态度：{plan.get("visual_attitude", "")}
母题/系统：{plan.get("visual_motif", "")}

现实场景层：
{page.get("real_scene", "")}

图解结构层：
{page.get("diagram_flow", "")}

文字层：
主标题：“{page.get("title", "")}”
辅助文字：“{page.get("body_text", "")}”
页码：{page.get("page", "")}

风格：
{plan.get("style_system", DEFAULT_STYLE_SYSTEM)}

色彩与材质：
{page.get("color_materials", plan.get("style_system", ""))}

避免出现：
{negative_prompts}
"""
    base += platform_guidance(plan)
    if is_ai_medical(plan):
        base += f"\n{AI_MEDICAL_ADDON}\n"
    return base


def render_plan_markdown(plan: dict[str, Any]) -> str:
    lines = [
        f"# {plan.get('topic', 'Visual Plan')}",
        "",
        "## 视觉方向",
        "",
        f"- 平台：{plan.get('platform')}",
        f"- 尺寸：{plan.get('width')}x{plan.get('height')}（{plan.get('aspect_ratio')}）",
        f"- 页数：{plan.get('page_count')}",
        f"- 审美风格：{plan.get('aesthetic_style', '研究档案式')}",
        f"- 受众：{plan.get('audience', '')}",
        f"- 核心判断：{plan.get('core_claim', '')}",
        f"- 视觉命题：{plan.get('visual_thesis', '')}",
        f"- 主角：{plan.get('protagonist', '')}",
        f"- 视觉态度：{plan.get('visual_attitude', '')}",
        f"- 母题/系统：{plan.get('visual_motif', '')}",
        "",
        "## 页面结构",
        "",
    ]

    for page in plan["pages"]:
        lines.extend(
            [
                f"### {page.get('page')} {page.get('title')}",
                "",
                f"- 正文：{page.get('body_text', '')}",
                f"- 视觉焦点：{page.get('visual_focus', '')}",
                f"- 现实场景：{page.get('real_scene', '')}",
                f"- 图解结构：{page.get('diagram_flow', '')}",
                "",
            ]
        )

    lines.extend(["## 质量检查", ""])
    for item in as_list(plan.get("quality_checklist")):
        lines.append(f"- [ ] {item}")

    lines.extend(["", "## 否决清单", ""])
    for item in as_list(plan.get("negative_prompts")):
        lines.append(f"- {item}")

    return "\n".join(lines) + "\n"


def write_outputs(plan: dict[str, Any], out_dir: Path) -> None:
    prompts_dir = out_dir / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "visual-plan.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (out_dir / "visual-plan.md").write_text(render_plan_markdown(plan), encoding="utf-8")

    for index, page in enumerate(plan["pages"], start=1):
        prompt = render_page_prompt(plan, page)
        (prompts_dir / f"page-{index:02d}.md").write_text(prompt, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="把 visual_plan.json 渲染成视觉方案和逐页提示词文件。")
    parser.add_argument("--input", required=True, type=Path, help="visual_plan.json 路径")
    parser.add_argument("--out-dir", required=True, type=Path, help="输出目录")
    parser.add_argument("--preset", choices=sorted(PRESETS), help="平台预设")
    parser.add_argument("--width", type=int, help="自定义宽度")
    parser.add_argument("--height", type=int, help="自定义高度")
    parser.add_argument("--aspect-ratio", help="自定义比例，例如 4:5")
    parser.add_argument("--page-count", type=int, help="自定义页数")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_plan = load_json(args.input)
    dimensions = pick_dimensions(raw_plan, args)
    plan = normalize_plan(raw_plan, dimensions)
    write_outputs(plan, args.out_dir)
    print(f"已生成 {len(plan['pages'])} 个提示词，输出目录：{args.out_dir}")


if __name__ == "__main__":
    main()
