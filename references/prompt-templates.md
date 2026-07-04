# 提示词模板

这些模板是结构，不是必须逐字照抄。画面内文字一定要短。

## visual_plan.json 结构

```json
{
  "topic": "",
  "audience": "",
  "platform": "xiaohongshu",
  "content_mode": "knowledge-card",
  "density": "balanced",
  "width": 1242,
  "height": 1660,
  "aspect_ratio": "3:4",
  "page_count": 6,
  "domain": "general",
  "aesthetic_style": "按领域选择：科技类蓝色冷感科技编辑风；医学类研究档案式",
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
{style_system}

色彩与材质：
{color_materials}

避免出现：
{negative_prompts}
```

## 小红书教程式知识卡片

用户要求教程式、多字多细节、操作手册、安装教程或不用 30% 删除时使用：

```text
小红书知识教程式单页，比例 {aspect_ratio}，尺寸 {width}x{height}，第 {page} 页。

内容模式：xhs-tutorial
信息密度：detailed，字多细节多，像可保存的操作手册；不做 30% 删除，只做去噪但不减信息。

视觉命题：{visual_thesis}
主角：{protagonist}
视觉态度：{visual_attitude}
母题/系统：{visual_motif}

现实场景层：
{real_scene}

教程结构层：
{diagram_flow}

文字层：
主标题：“{title}”
辅助文字：“{body_text}”
页码：{page}
必要时加入：步骤编号、速查表、命令行、表单、便签、红笔批注、仓库链接、真实操作截图感。

风格：
{style_system}

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

## PPT 信息密度追加

`ppt-slide` 默认追加 `minimal`。用户要求“字多细节多、教程页、培训页”时追加 `detailed`。

```text
PPT 信息密度：{density}
minimal：字少、留白多、重点突出，适合投影观看；辅助文字不超过两句，流程节点 3-5 个。
balanced：保留 2-4 条说明，有清楚标题、主视觉和少量解释。
detailed：字多细节多，像课程讲义或教程页；允许步骤、速查表、批注和证据材料，但必须分区清楚、手机和投影都可读。
```

## AI+医学补充

AI+医学题材追加：

```text
AI+医学模式：表现为可追责的临床协作系统。画面中有医生、报告、病历、影像或随访材料作为真实语境。AI 只作为辅助分析层，不是最终决策者。医生确认、审核状态、责任链和随访闭环必须可见。病历和报告不能出现可识别个人信息。避免机器人医生、AI 大脑、赛博医院、神奇诊断、AI 自主治疗暗示。
```

## 科技冷蓝补充

科技、AI、开发工具、模型、算力、Agent、产品架构类题材优先追加：

```text
科技冷蓝模式：蓝色冷感科技编辑风。冷蓝、钢蓝、蓝灰和纸白为主，真实开发工作台、IDE代码窗口、模型选择器、终端日志、任务清单、评估材料和产品架构草图形成多层编辑视觉。保留小字细节和材料密度，让画面有精细的工程质感，但主标题必须清楚。真实桌面纵深、浅景深、自然冷光、少量绿色状态点、极少量橙红风险标记。避免本地渲染卡片、纯文字海报、机器人、AI大脑、赛博城市、蓝紫渐变SaaS模板、随机3D图标、品牌Logo、具体假跑分、假价格、假日期、假排名表。
```

## 默认研究档案式风格文本

医学或其他默认研究档案式主题，使用这段作为 `style_system`：

```text
研究档案式编辑设计。纸白和冷灰为底，理性蓝结构线，克制黑色标题，真实工作材料，证据层次，轻微颗粒质感，只在帮助理解时加入少量手写批注、圈画、对号/叉号或签字笔痕迹。画面先结构后装饰，少字，高层级，避免通用AI海报感、蓝紫渐变科技风、3D图标堆和PPT卡片感。
```

## 默认科技冷蓝风格文本

科技类主题，优先使用这段作为 `style_system`：

```text
蓝色冷感科技编辑风。冷蓝、钢蓝、蓝灰和纸白为主，真实开发工作台、IDE代码窗口、模型选择器、终端日志、任务清单、评估材料和产品架构草图形成多层编辑视觉。保留小字细节和材料密度，让画面有精细的工程质感，但主标题必须清楚。真实桌面纵深、浅景深、自然冷光、少量绿色状态点、极少量橙红风险标记。整体像科技媒体专题图文和高级知识卡，不像本地渲染图、PPT流程图或蓝紫渐变SaaS海报。
```
