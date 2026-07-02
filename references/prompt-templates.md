# 提示词模板

这些模板是结构，不是必须逐字照抄。画面内文字一定要短。

## visual_plan.json 结构

```json
{
  "topic": "",
  "audience": "",
  "platform": "xiaohongshu",
  "width": 1242,
  "height": 1660,
  "aspect_ratio": "3:4",
  "page_count": 6,
  "domain": "general",
  "core_claim": "",
  "visual_thesis": "",
  "protagonist": "",
  "visual_attitude": "",
  "visual_motif": "",
  "style_system": "",
  "negative_prompts": [],
  "pages": [
    {
      "page": "01/06",
      "title": "",
      "body_text": "",
      "visual_focus": "",
      "real_scene": "",
      "diagram_flow": "",
      "text_layer": "",
      "color_materials": "",
      "negative_prompts": []
    }
  ],
  "quality_checklist": []
}
```

## 多页知识卡片

```text
知识卡片单页，比例 {aspect_ratio}，尺寸 {width}x{height}，第 {page} 页。

视觉命题：{visual_thesis}
主角：{protagonist}
视觉态度：{visual_attitude}
母题/系统：{visual_motif}

现实场景层：
{real_scene}

图解结构层：
{diagram_flow}

文字层：
主标题：“{title}”
辅助文字：“{body_text}”
页码：{page}

风格：
研究档案式编辑设计。纸白和冷灰为底，理性蓝结构线，克制黑色标题，真实工作材料，证据层次，轻微颗粒质感，只在帮助理解时加入少量手写批注。

色彩与材质：
{color_materials}

避免出现：
{negative_prompts}
```

## 单张图 / Hero 图

```text
编辑设计视觉图，比例 {aspect_ratio}，尺寸 {width}x{height}。

核心判断：{core_claim}
视觉命题：{visual_thesis}
主角：{protagonist}
视觉态度：{visual_attitude}

画面用一个清楚的中心场景组织信息：真实材料第一层，图解/证据叠加第二层，短句观点第三层。缩小到预览尺寸时仍能看懂。

画面文字：
标题：“{title}”
辅助：“{body_text}”

风格与材质：
{style_system}
{color_materials}

避免出现：
{negative_prompts}
```

## AI+医学补充

AI+医学题材追加：

```text
AI+医学模式：表现为可追责的临床协作系统。画面中有医生、报告、病历、影像或随访材料作为真实语境。AI 只作为辅助分析层，不是最终决策者。医生确认、审核状态、责任链和随访闭环必须可见。病历和报告不能出现可识别个人信息。避免机器人医生、AI 大脑、赛博医院、神奇诊断、AI 自主治疗暗示。
```
