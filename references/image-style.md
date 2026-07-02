# Image Style / 配图规范

## 中文

### 核心标准

每张图必须满足：

1. 只承担一个明确的信息任务。
2. 一张图对应一个高光、一个章节观点，或全场总回顾。
3. 中文标题清晰但克制，不做“大字压全屏”的海报。
4. 层级清楚：标题、副标题、模块标题、小标签。
5. 必须有图解、流程、对比、白板、会议复盘或证据结构。
6. 全套图风格统一。
7. 不生成假二维码、假 Logo、假官方背书、水印或未授权品牌标识。
8. 所有信息忠于逐字稿和文章。
9. 不生成真实名人或嘉宾肖像；使用抽象剪影、3D 泥塑小人、图标、屏幕、便签和符号化场景。

保留用户反馈标准：图文表达清楚，适合小红书，看着不累，很清晰，也能知道意思。

### 字号和比例硬规则

- 禁止使用无边界词：`giant`、`huge`、`largest`、`occupying 40% of the canvas`，除非用户明确要超大字海报。
- 公众号 16:9 章节解释图：标题区约占画面高度 `12%-18%`。
- 公众号第一张图必须是封面图，比例固定为 `2.35:1`，推荐 `1410 x 600` 或等比例。
- 公众号封面标题区最多 `20%-28%`，主体信息必须留在中心安全区。
- 小红书 3:4 图卡：标题区约占画面高度 `14%-22%`。
- 副标题约为主标题字号的 `30%-40%`。
- 模块标题约为主标题字号的 `40%-55%`。
- 小标签/说明约为主标题字号的 `22%-32%`。
- 主体图解、流程和信息模块的视觉重量必须大于标题。
- 如果标题看起来超过全图视觉重量的三分之一，必须重写 Prompt 或改用本地排版。

### 参考图比例

用户提供的 GrowthOS 横版参考图通常接近 `1080 x 608`。学习这些比例：

- 主标题字高约占画布高度 `10%-14%`。
- 副标题字高约占 `3.5%-5%`。
- 标题区总高度约 `18%-24%`，不得超过 `28%`。
- 中央信息图区域约 `50%-65%`，必须是视觉主体。
- 底部策略条约 `8%-12%`。

不要把“参考图风格”误解成“把标题做很大”。这些图好看的关键是：克制标题 + 高密度但清楚的中央信息图。

### 平台约束

- 公众号正文图：默认 16:9 或接近 16:9 横图，适合 390px 宽手机阅读。
- 公众号封面：第一张图，固定 `2.35:1`，设计时考虑大卡片和缩略图裁切，核心标题和主体留在中心安全区。
- 小红书：默认 3:4 竖图，常用 `1080 x 1440` 输出，避免密集小字。
- 每张图优先：一个标题、一个副标题、3-5 个模块标题、3-4 个底部说明项。

平台通常不会给“配图字体字号表”。因此本 Skill 使用画布高度比例和用户参考图比例作为设计约束。

### GrowthOS 参考风格

- 背景：米白纸质、轻微颗粒。
- 边角：橙色/黑色撕纸、胶带、网格/点阵碎片。
- 字体：粗黑中文标题，关键词橙红色。
- 构图：顶部克制标题，中间流程/会议/工作台/设备图解，左右证据卡，底部解释条。
- 人物：优先使用 3D 泥塑协作者，低细节、无真实五官、橙/黑/米色衣服，围绕手机、白板、卡片协作。
- 信息密度：4-6 个信息块比一个大图标加一句口号更好。

### 公众号标题主色同步

公众号文章标题块和生成图片必须使用同一主色。默认主色为 GrowthOS 橙红 `#E6532E`；如果图片套图换成绿色、蓝色或其他主色，文章标题块的左侧强调色也必须同步切换。

标题块采用用户截图式样：

- 左侧一条竖向主色条，宽度约为标题块宽度的 `0.6%-1%`。
- 标题块背景使用极浅色底，例如 `#FFF5EF` 或主色 `6%-10%` 透明度。
- 标题文字使用深墨色，避免彩色整句大标题。
- 标题字号克制，移动端阅读时一行或自然换行，不做海报式超大字。
- 文章内同级标题、封面图、章节图的主色必须一致。

避免：蓝紫赛博朋克、纯机器人主视觉、真实肖像、空洞 AI 概念、假水印、假二维码、假 Logo、超大两行口号、空白中区。

### 信息块文案标准

信息块必须有具体策略，不只写名词。

好例子：

- `先测词库` / `看不同地区账号和画像下的曝光度`
- `进相关帖子` / `截取已经被需求筛过的精准流量`
- `筛红人画像` / `按粉丝量、近 7 天内容、国家和品类匹配`
- `建设可引用内容` / `把品牌放到 AI 更可能引用的平台`
- `MVP 先验证` / `用图片/视频 + prompt 先看结果`
- `跑反馈闭环` / `触达、试用、反馈、迭代后再放大`

坏例子：

- `GEO`
- `红人营销`
- `反馈`
- `增长`

单词标签只能作为导航小标签，不能作为模块主体内容。

### 图片来源和文字控制

除非运行路径明确可验证，不要声称使用了具体模型。

每套最终图必须记录：

- `model/source`：内置图片工具、明确 GPT Image API/CLI、用户参考图、本地合成或本地渲染。
- `composition`：中文文字、字号、策略块是否本地排版。
- `final file`：最终图片在工作区的路径。

当中文文字准确性、字号比例或标题克制程度很重要时，优先两步法：先用图片模型生成无字视觉，再本地排版中文。不要让模型自由发明或缩放中文文字。

### 总回顾图

每次都要在章节图前加入 `00-overview-recap`。

目标：让没参加的人一眼看懂这个房间是谁在聊、聊了什么、为什么重要、大家问了什么、最后留下什么判断。

内容规则：

1. 只提取逐字稿、文章和最终高光中出现的具体信息。
2. 过滤寒暄、设备测试、重复确认和低价值闲聊。
3. 包含人物、角色、项目、工具、场景、真实问题、方法、风险和结论。
4. 不虚构链接、公司全名、数据、隐私身份、会议开始时间、房间人数。
5. 真实公司没有公开授权时，用泛化标签。
6. 不出现私密凭证、电话、私密 URL 或敏感操作细节。

结构建议：

- 左上角：概括本场讨论核心的标题。
- 中央：2-4 位关键人物在会议房间/圆桌/屏幕共享场景里。
- 周围：发起人、分享者、提问者、共创者和参与者模块。
- 右侧：3-5 个核心模块，如核心挑战、现场反馈、关键工具、服务对象、共创结果。
- 下方：讨论路径、平台选择、风险提醒和最终结论。

### 小红书图卡

默认 7 张：

1. 封面：强钩子 + 核心视觉。
2. 痛点/背景。
3. 洞察。
4. 方法/流程。
5. 案例。
6. 社群/活动。
7. 总结/CTA。

小红书每页文字尽量短：主标题 8-16 个字，副标题 1-2 行，流程页 3-5 个节点。

### 必须输出的 `image-prompts.md`

`image-prompts.md` 必须包含：

1. `Style Reference Notes`：参考图学习记录。
2. `Unified Master Prompt`：统一风格母 Prompt。
3. `WeChat Prompt Set`：总回顾、封面、所有章节解释图。
4. `Xiaohongshu Prompt Set`：每张小红书卡片。
5. `QR/CTA Composition Notes`：二维码必须用真实文件合成。

### 统一母 Prompt

```text
公众号封面图，横版 2.35:1，推荐 1410 x 600，是文章第一张图。公众号正文配图，横版 16:9。适合手机阅读。
小红书图文笔记配图，竖版 3:4。适合手机阅读。

画面信息清晰，构图有中心视觉，留白充足。中文标题必须清晰可读但克制，章节图标题区只占画面高度 12%-18%，公众号封面标题区最多 20%-28%，不要夸张巨大。
统一风格：米白纸质背景，手绘白板会议纪要 + 模板信息图 + 现场插画，撕纸拼贴边角，胶带便签，粗黑中文标题，橙色强调关键词，少量绿色/蓝色用于流程、检查和增长信号。公众号文章标题块使用同一主色：左侧主色竖条 + 极浅色底 + 深色标题文字。
主体信息图的视觉权重必须大于标题。
不要真实人物肖像，不要生成明星本人；人物优先使用 3D 泥塑协作者风格。
不要水印，不要二维码，不要品牌 logo，不要虚构公司名、数据、链接、隐私身份。
```

### 二维码处理

永远不要用 AI 生成或重绘二维码。

步骤：

1. 读取用户提供的真实二维码。
2. 等比缩放，保持码点清晰。
3. 放在纯白或浅色纸片底。
4. 不模糊、不变形、不让阴影覆盖码点。
5. 合成后人工目测。

## English

### Core Standard

Every image must satisfy:

1. One clear information task.
2. One highlight, chapter idea, or whole-session recap per image.
3. Readable but restrained Chinese title.
4. Clear hierarchy: title, subtitle, module titles, small labels.
5. A diagram, workflow, comparison, whiteboard, meeting recap, or evidence structure.
6. Unified style across the set.
7. No fake QR code, fake logo, fake endorsement, watermark, or unauthorized brand mark.
8. Faithful to transcript evidence and article content.
9. No real celebrity or speaker portrait; use abstract silhouettes, 3D clay figures, icons, screens, sticky notes, and symbolic scenes.

Preserve the user standard: clear visual expression, suitable for Xiaohongshu, not tiring to read, and easy to understand.

### Typography Guardrails

- Do not use unbounded size words like `giant`, `huge`, `largest`, or `occupying 40% of the canvas` unless the user explicitly requests an oversized typography poster.
- WeChat 16:9 chapter image: title zone about `12%-18%` of canvas height.
- The first WeChat image must be the cover image with fixed `2.35:1` ratio, recommended `1410 x 600` or equivalent.
- WeChat cover: title zone at most `20%-28%`, with key subject in the central safe area.
- Xiaohongshu 3:4 card: title zone about `14%-22%`.
- Subtitle should be about `30%-40%` of main title size.
- Module headers should be `40%-55%` of main title size.
- Small labels should be `22%-32%` of main title size.
- The central diagram, workflow, and information modules must carry more visual weight than the headline.
- If the title feels like more than one third of the whole visual weight, revise the prompt or typeset locally.

### Reference Ratios

For GrowthOS-style landscape references around `1080 x 608`:

- Main title glyph height: about `10%-14%` of canvas height.
- Subtitle glyph height: about `3.5%-5%`.
- Total title zone: about `18%-24%`, never above `28%`.
- Central information diagram: about `50%-65%`; this must be the visual subject.
- Bottom strategy strip: about `8%-12%`.

Do not infer the reference style as "make the title huge." The quality comes from a restrained headline plus a dense but clear central information diagram.

### Platform Constraints

- WeChat inline images: 16:9 or near-16:9 landscape, readable on a 390px mobile screen.
- WeChat cover: first image, fixed `2.35:1`; keep core title and subject in the central safe area for feed and thumbnail crops.
- Xiaohongshu: 3:4 vertical cards, commonly `1080 x 1440`; avoid dense tiny text.
- Prefer one title, one subtitle, 3-5 module headers, and 3-4 bottom explanation items.

Platforms usually do not provide a useful illustration font-size table. This skill therefore uses canvas-height ratios and user reference-image ratios as design constraints.

### GrowthOS Reference Style

- Background: warm off-white paper with subtle grain.
- Edges: orange/black torn paper, tape, grid/dot scraps.
- Typography: bold black Chinese title with orange-red keywords.
- Composition: restrained top title, central workflow/meeting/workbench/device diagram, side evidence cards, bottom explanation strip.
- People: prefer low-detail 3D clay collaborator figures with no real facial identity, wearing orange/black/beige, collaborating around phones, boards, or cards.
- Density: 4-6 information blocks are better than one large icon plus slogan.

### WeChat Title Accent Color

The WeChat article title block and generated images must share the same dominant accent color. Default GrowthOS accent is orange-red `#E6532E`. If the image set uses green, blue, or another dominant accent, the article title block's left accent bar must use the same color.

Use the screenshot-style title block:

- A vertical accent bar on the left, about `0.6%-1%` of the title block width.
- A very light background such as `#FFF5EF` or the accent color at `6%-10%` opacity.
- Deep ink title text, not a fully colored headline.
- Restrained mobile-readable font size with natural wrapping.
- Same-level article headings, cover image, and chapter images must share the dominant accent color.

Avoid cyberpunk, robot-only visuals, realistic portraits, empty AI concepts, fake watermarks, fake QR codes, fake logos, oversized two-line slogans, and empty center areas.

### Strategy Block Copy

Every module should carry concrete strategy, not generic nouns. Use transcript-backed content with an action verb, a concrete object, and a reason/output/observable metric.

Good examples and bad examples are the same as the Chinese section above.

### Image Provenance And Text Control

Do not claim a specific model unless the model path is explicit and verifiable.

For each final image set, record:

- `model/source`: built-in image tool, explicit GPT Image API/CLI, user reference image, local composition, or local renderer.
- `composition`: whether Chinese text, typography, and strategy blocks were locally typeset.
- `final file`: workspace path for each deliverable image.

When exact Chinese text, typography proportions, or transcript-backed strategy copy are required, prefer a two-step workflow: generate text-free visuals with the image model, then typeset final Chinese locally.

### Whole-Session Recap Image

Always add `00-overview-recap` before chapter images.

Purpose: let a reader who did not attend quickly understand who was in the room, what was discussed, why it mattered, what questions appeared, and what judgment remained.

Use only concrete information from the transcript, article, and final highlights. Filter greetings and low-value noise. Do not invent links, company full names, metrics, private identity details, meeting start time, room size, or participant scale.

Suggested structure: title at top-left, 2-4 key people in a meeting/screen-share scene in the center, people/topic/question/tool modules around the center, 3-5 core modules on the right, discussion path and final conclusion at the bottom.

### Xiaohongshu Cards

Default 7-card set:

1. Cover: strong hook and core visual.
2. Pain/background.
3. Insight.
4. Method/workflow.
5. Case.
6. Community/event.
7. Summary/CTA.

Keep text short: 8-16 Chinese characters for main title when possible, 1-2 subtitle lines, and 3-5 nodes for workflow pages.

### Required `image-prompts.md`

`image-prompts.md` must include style notes, unified master prompt, WeChat prompt set, Xiaohongshu prompt set, and QR/CTA composition notes.

### QR Handling

Never generate or redraw QR codes with AI. Load the real user-provided QR image, resize proportionally, place it on a light card, keep modules crisp, and inspect the result visually.

## Source Links / 参考链接

- WeChat draft workflow / 微信草稿箱流程：`https://developers.weixin.qq.com/doc/service/guide/product/draft.html`
- WeChat Official Account docs / 微信公众号文档：`https://developers.weixin.qq.com/doc/offiaccount/`
- Xiaohongshu creator platform / 小红书创作服务平台：`https://creator.xiaohongshu.com/`
- NN/g scanning behavior / 网页扫读研究：`https://www.nngroup.com/articles/how-users-read-on-the-web/`
