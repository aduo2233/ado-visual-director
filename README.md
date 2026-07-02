# ado-visual-director

阿多小筑视觉导演 Skill。它把选题、文章或创意简报，转成一套有审美判断的视觉方案和图片提示词包。

它沉淀的是一种中文内容创作者可复用的 taste：研究档案式编辑设计、清楚的视觉命题、真实材料层次、克制构图，以及 AI+医学等专业场景的视觉边界。

## 安装

```bash
cd ~/.codex/skills
git clone https://github.com/<your-github-username>/ado-visual-director.git
```

如果仓库放在别处，也可以用软链接：

```bash
ln -s /path/to/ado-visual-director ~/.codex/skills/ado-visual-director
```

## 使用

在 Codex 里这样说：

```text
Use $ado-visual-director 把这个 AI+医学选题做成 4 页小红书视觉方案，尺寸 1080x1350。
```

也可以说：

```text
用 ado-visual-director 给这篇文章做一套小红书知识卡片提示词。
```

这个 skill 默认输出视觉导演方案、逐页结构、图片提示词和质量检查清单，不直接调用生图模型。

## 渲染提示词包

如果已经有 `visual_plan.json`，可以生成标准文件包：

```bash
python3 scripts/render_prompt_pack.py --input visual_plan.json --out-dir output
```

常用参数：

```bash
python3 scripts/render_prompt_pack.py \
  --input visual_plan.json \
  --out-dir output \
  --preset xiaohongshu \
  --page-count 6
```

```bash
python3 scripts/render_prompt_pack.py \
  --input visual_plan.json \
  --out-dir output \
  --width 1080 \
  --height 1350 \
  --aspect-ratio 4:5
```

## 输出内容

脚本会生成：

- `visual-plan.md`：可读版视觉方案
- `visual-plan.json`：机器可读版视觉方案
- `prompts/page-01.md` 等逐页图片提示词
