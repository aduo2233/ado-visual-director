# ado-visual-director

阿多小筑视觉导演 Skill。它把一个选题、文章、公众号草稿、产品想法或创意简报，转成一套有审美判断的视觉方案和图片提示词包。

它沉淀的是一种中文内容创作者可复用的 taste：研究档案式编辑设计、清楚的视觉命题、真实材料层次、克制构图，以及 AI+医学等专业场景的视觉边界。

这个 skill 默认不直接生成图片，也不绑定任何生图模型。它负责先把“图应该怎么想、怎么构成、怎么避免廉价感”说清楚，再输出可以交给 ChatGPT 图像模型、Midjourney、即梦、可灵、豆包、混元等工具使用的提示词。

## 适合做什么

- 把一个选题做成小红书知识卡片视觉方案。
- 把公众号文章拆成 4 页、6 页或 8 页图文提示词。
- 给 AI+医学、AI产品、Agent、工作流、评估、医疗产品等主题做专业视觉方向。
- 为单张海报、封面图、横版 Hero 图生成视觉导演方案。
- 为 PPT、课程、演讲、汇报生成 16:9 单页配图提示词。
- 给已有图片方案做审美检查：删掉模板感、PPT感、机器人医生、AI大脑、蓝紫渐变等廉价套路。
- 按自定义尺寸输出提示词，比如 `1080x1350`、`1242x1660`、`1920x1080`。

## 安装

### 从 GitHub 安装

```bash
cd ~/.codex/skills
git clone git@github.com:aduo2233/ado-visual-director.git
```

如果你没有配置 GitHub SSH，也可以用 HTTPS：

```bash
cd ~/.codex/skills
git clone https://github.com/aduo2233/ado-visual-director.git
```

### 从本地仓库安装

如果仓库已经在别的位置，可以创建软链接：

```bash
ln -s /path/to/ado-visual-director ~/.codex/skills/ado-visual-director
```

当前本机已经链接到：

```text
/Users/dumingjing/.codex/skills/ado-visual-director
```

## 最简单的用法

在 Codex 里直接点名这个 skill：

```text
Use $ado-visual-director 把这个选题做成一套小红书知识卡片视觉方案：AI医学产品为什么不能画成机器人医生
```

也可以自然一点说：

```text
用 ado-visual-director 给这篇文章做一套小红书图片提示词，6页，尺寸1242x1660。
```

如果是 AI+医学主题，可以这样说：

```text
Use $ado-visual-director 把“AI辅助影像诊断如何进入临床工作流”做成4页小红书视觉方案，尺寸1080x1350。
```

## 推荐输入格式

你可以只给一个选题，也可以给更完整的信息。信息越清楚，输出越稳定。

```text
Use $ado-visual-director

主题：AI辅助影像诊断为什么不能被画成机器人医生
受众：医疗AI产品经理、医院信息化负责人
平台：小红书
页数：4页
尺寸：1080x1350
希望的感觉：专业、克制、真实临床场景、有责任链
不要出现：机器人医生、AI大脑、赛博医院
```

也可以直接贴文章：

```text
Use $ado-visual-director

请把下面这篇文章拆成6页小红书知识卡片，尺寸1242x1660。
要求：研究档案式编辑设计，少文字，有真实材料层次，每页一个重点。

文章：
……
```

## 典型使用场景

### 1. 小红书知识卡片

```text
Use $ado-visual-director 把这个主题做成6页小红书知识卡片：
普通人学AI，不要先追模型，先学会拆工作流。
尺寸1242x1660。
```

会输出：

- 视觉命题
- 主角
- 视觉态度
- 视觉母题或视觉系统
- 6页页面结构
- 每页图片提示词
- 否决清单
- 30%删除实验检查

### 2. AI+医学视觉方案

```text
Use $ado-visual-director 做一套AI+医学视觉方案：
主题是“AI辅助诊断真正重要的是医生确认和随访闭环”。
做4页，尺寸1080x1350。
```

AI+医学模式会自动强调：

- 可追责的临床协作系统
- 医生确认是关键节点
- 病历和报告不能有可识别个人信息
- AI只是辅助分析层，不是最终诊断主体
- 避免机器人医生、AI大脑、赛博医院、万能诊断机器

### 3. 横版封面 / Hero 图

```text
Use $ado-visual-director 给这个主题做一张横版Hero图提示词：
AI工作流，不是魔法。
尺寸1920x1080。
```

适合用于：

- 网站首屏图
- 文章封面
- 演示文稿封面
- 视频开场视觉

### 4. PPT 单页配图

```text
Use $ado-visual-director 给这个主题做一张PPT演示页配图：
AI医学产品真正重要的是责任链，而不是机器人医生。
使用ppt-slide预设。
```

PPT 预设会默认使用：

- 尺寸：`1920x1080`
- 比例：`16:9`
- 页数：`1`
- 排版：标题区 + 主视觉区 + 少量辅助说明
- 要求：适合投影观看，安全边距充足，大标题远距离可读，流程节点控制在 3-5 个

它会避免：

- 企业汇报 PPT 感
- 复杂表格
- 密集小字
- 装饰性卡片堆
- 图标堆砌

### 5. 审美检查和改稿

```text
Use $ado-visual-director 检查下面这组图片提示词，帮我去掉模板感和廉价AI视觉套路。

提示词：
……
```

它会重点检查：

- 是否有视觉命题
- 主角是否明确
- 是否满屏小字
- 是否有 PPT 卡片感
- 是否过度依赖蓝紫渐变
- 是否出现机器人、AI大脑、3D图标堆
- 是否完成 30% 删除实验

## 默认尺寸预设

| 预设 | 尺寸 | 比例 | 默认页数 | 用途 |
| --- | --- | --- | ---: | --- |
| `xiaohongshu` | 1242x1660 | 3:4 | 6 | 小红书竖版知识图文 |
| `square` | 1080x1080 | 1:1 | 1 | 方图 |
| `portrait-social` | 1080x1350 | 4:5 | 4 | 竖版社媒图 |
| `wide-hero` | 1920x1080 | 16:9 | 1 | 横版封面、Hero 图 |
| `ppt-slide` | 1920x1080 | 16:9 | 1 | PPT 单页配图、演讲页、课程页 |

用户明确给出尺寸时，优先使用用户尺寸。

## 输出会长什么样

常规输出包括：

```text
1. 视觉导演方案
   - 核心判断
   - 视觉命题
   - 主角
   - 视觉态度
   - 视觉母题/视觉系统
   - 风格系统
   - 否决清单

2. 逐页结构
   - 页码
   - 标题
   - 辅助文字
   - 现实场景层
   - 图解结构层
   - 文字层

3. 逐页图片提示词
   - 每页一条完整提示词
   - 包含尺寸、比例、页码、主视觉、风格、禁止元素

4. 质量检查
   - 是否每页只讲一个意思
   - 是否有真实材料层次
   - 是否避免廉价AI套路
   - 是否完成30%删除实验
```

## 使用脚本生成提示词包

这个仓库里有一个脚本：

```text
scripts/render_prompt_pack.py
```

它的作用是把一个已经写好的 `visual_plan.json` 渲染成标准文件包：

```text
output/
├── visual-plan.md
├── visual-plan.json
└── prompts/
    ├── page-01.md
    ├── page-02.md
    └── ...
```

### 基础命令

```bash
python3 scripts/render_prompt_pack.py --input visual_plan.json --out-dir output
```

### 指定小红书预设

```bash
python3 scripts/render_prompt_pack.py \
  --input visual_plan.json \
  --out-dir output \
  --preset xiaohongshu
```

### 指定 PPT 单页预设

```bash
python3 scripts/render_prompt_pack.py \
  --input visual_plan.json \
  --out-dir output \
  --preset ppt-slide
```

### 自定义尺寸和页数

```bash
python3 scripts/render_prompt_pack.py \
  --input visual_plan.json \
  --out-dir output \
  --width 1080 \
  --height 1350 \
  --aspect-ratio 4:5 \
  --page-count 4
```

## visual_plan.json 示例

```json
{
  "topic": "AI辅助影像诊断的责任链",
  "audience": "医疗AI产品经理",
  "platform": "portrait-social",
  "domain": "AI+医学",
  "core_claim": "AI医学产品必须把责任链画清楚",
  "visual_thesis": "所有注意力都应该留给被医生确认的临床证据",
  "protagonist": "医生确认过的影像报告和责任链",
  "visual_attitude": "责任、边界、照护、克制",
  "visual_motif": "病历夹与审核流程",
  "style_system": "研究档案式编辑设计，纸白冷灰，理性蓝结构线，少量红色审核批注",
  "negative_prompts": ["机器人医生", "AI大脑", "赛博医院", "可识别患者信息"],
  "pages": [
    {
      "page": "01/04",
      "title": "不是机器人医生",
      "body_text": "AI只作为辅助分析层",
      "visual_focus": "医生确认过的影像报告",
      "real_scene": "诊室桌面、病历夹、影像片、无个人信息的结构化报告、审核印章",
      "diagram_flow": "患者就诊 -> 影像采集 -> AI辅助分析 -> 医生确认 -> 随访闭环",
      "color_materials": "纸白冷灰、蓝色结构线、绿色确认、橙红风险标记"
    }
  ],
  "quality_checklist": ["医生确认节点清晰", "没有自主诊断暗示", "30%删除实验已完成"]
}
```

## 常见问题

### 为什么要写 `Use $ado-visual-director`？

这样 Codex 会明确加载这个 skill 的方法论和参考文件。如果你只说“帮我做图”，它可能不会自动使用这套审美系统。

### 它会直接生成图片吗？

默认不会。它生成的是视觉方案和图片提示词。你可以把提示词复制到任何生图工具里使用。

### 能不能指定尺寸？

可以。直接写：

```text
尺寸1080x1350
```

或：

```text
比例4:5，4页
```

### 能不能用于非医学主题？

可以。AI+医学只是一个专门模式。普通 AI 产品、Agent、工作流、评估、内容创作、产品方法论，都可以用。

### 如果生成结果太复杂怎么办？

让它重新做 30% 删除实验：

```text
Use $ado-visual-director 对刚才的方案做30%删除实验，删掉装饰和重复信息，让主角更清楚。
```

## 许可证

MIT License，Copyright (c) 2026 aduo2233。
