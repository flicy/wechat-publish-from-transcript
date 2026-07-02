# Product Notes / 产品说明

## 中文

### 产品定位

`wechat-publish-from-transcript` 是一个面向内容运营、社群主理人、播客/直播复盘者和增长团队的多平台 Agent Skill / workflow package。它把“逐字稿到公众号发布”做成可执行链路，而不是一次性的写作提示词，并可通过 Codex、Cursor、Cola、Claude 等环境加载。

### 解决的问题

1. 用户通常只有逐字稿，没有整理好的高光。
2. 公众号长文需要证据、结构、配图和发布检查，不只是文案。
3. Image 2.0 / GPT Image 容易把中文标题做得过大，或者把公众号横图误生成小红书竖图。
4. 二维码、Logo、私密信息不能交给模型重绘或泄露。
5. 公众号草稿箱提交需要独立的确认流程和脚本封装，并且应尽量少消耗 token。
6. 同一场内容还要同步扩展到小红书和 X，不应重复读逐字稿。

### vNext 迭代内容

- 输入契约升级：逐字稿是唯一必需输入，用户不再需要手工给高光。
- 高光引擎升级：引入 10 维评分，并把微信“最多在线观众、最高评论率、最高留存率”等平台信号作为加权参考。
- 配图系统升级：每篇文章必须有 `00-overview-recap` 总回顾图。
- 设计规范升级：公众号第一张图固定为 `2.35:1` 封面图；章节图标题区 12%-18%，封面标题区最多 20%-28%，小红书标题区 14%-22%。
- 公众号标题样式升级：文章标题块和图片主色保持一致，采用左侧主色条 + 浅色底的截图式标题样式。
- 参考图学习升级：保留 GrowthOS 米白纸、橙黑撕纸、手绘信息图、3D 泥塑协作者的风格。
- 图片来源升级：必须记录图片来源、模型路径或本地排版方式。不能无依据声称使用了某个具体模型。
- 发布链路升级：新增 `build_wechat_publish_ready.py` 和 `submit_wechat_draft.sh`。
- 内容确认升级：提交草稿前必须检查标题、摘要、封面、图片、姓名、二维码、密钥和评论设置。
- 并行发布升级：文章和图片确认后，启动微信草稿 Agent 与小红书帖子 Agent 两个同步任务。
- Token 节省升级：并行子任务只读取 `publish-ready.md`、图片清单和 `content-pack.json`，不重新读取完整逐字稿。
- 跨平台升级：每次输出 `social-pack/content-pack.json`，并生成 `xiaohongshu/post.md`，为小红书和 X 留出结构化接口。
- 安装适配升级：新增 `installation.md`，说明 Codex、Cursor、Cola、Claude 和通用 `AGENTS.md` 的接入方式；Cola 支持直接导入自定义 Skill 包。
- 文档升级：Skill 包内 Markdown 文档全部中英双语，方便中文团队使用，也方便未来英文协作者审阅。

### 核心交付物

- `plan.md`：执行计划。
- `highlight-candidates.md`：候选高光。
- `highlight-scorecard.md`：高光评分。
- `platform-highlight-signals.md`：平台高光信号。
- `evidence-map.md`：证据映射。
- `article-source.md`：文章源稿。
- `article-publish.md`：公众号发布稿。
- `image-plan.md`：配图计划。
- `image-prompts.md`：公众号/小红书图片 Prompt 包。
- `style-reference-notes.md`：参考图学习记录。
- `wechat/publish-ready.md`：微信 API 草稿输入稿。
- `wechat/draft-submit-report.md`：草稿提交结果。
- `xiaohongshu/post.md`：小红书帖子初稿。
- `xiaohongshu/card-sequence.md`：小红书图卡顺序。
- `social-pack/content-pack.json`：跨平台内容包。
- `references/installation.md`：多平台安装说明。

### 非目标

- 不自动正式群发公众号文章，除非用户单独明确要求。
- 不自动生成或重绘二维码。
- 不凭空补公司全名、数据、链接或敏感身份。
- 不保证每个平台都有原生 Skill Registry；没有原生 Skill 机制的平台通过 Rules、项目说明或 `AGENTS.md` 适配。
- 不保证小红书自动发布，除非后续接入发布工具或登录态。

### 未来 X Skill 扩展

后续可以基于 `social-pack/content-pack.json` 独立实现 `publish-to-x-from-content-pack`：

1. 读取 strongest hook 作为 Post 1。
2. 把公众号章节压缩成 6-10 条 thread。
3. 每条配图不超过 4 张。
4. 为图片生成 alt text。
5. 二维码图不作为 X 主图，优先链接文章。
6. 输出 `x/thread.md`、`x/assets.json` 和发布报告。

## English

### Product Positioning

`wechat-publish-from-transcript` is a multi-platform Agent Skill / workflow package for content operators, community builders, podcast/livestream recap creators, and growth teams. It turns "transcript to WeChat article" into an executable publishing pipeline rather than a one-off writing prompt, and it can be loaded from Codex, Cursor, Cola, Claude, and similar environments.

### Problems It Solves

1. Users usually only have a transcript, not curated highlights.
2. WeChat longform publishing needs evidence, structure, images, and preflight checks, not just copy.
3. Image 2.0 / GPT Image may oversize Chinese headlines or generate vertical Xiaohongshu-style images for WeChat prompts.
4. QR codes, logos, and private information must not be regenerated or leaked by the model.
5. WeChat draft submission needs a separate confirmation flow and helper scripts while keeping token usage low.
6. The same talk often needs to expand to Xiaohongshu and X in parallel without re-reading the whole transcript.

### vNext Iteration

- Input contract: the transcript is the only required input; users do not need to manually provide highlights.
- Highlight engine: adds a 10-dimension scorecard and uses platform signals such as most online viewers, highest comment rate, and highest retention rate.
- Image system: every article includes a `00-overview-recap` whole-session image.
- Design spec: the first WeChat image is a fixed `2.35:1` cover; WeChat chapter title zone 12%-18%, cover title zone at most 20%-28%, Xiaohongshu title zone 14%-22%.
- WeChat title style: article title blocks and images share the same accent color, using a screenshot-like left accent bar plus pale background.
- Reference-style learning: preserves GrowthOS off-white paper, orange/black torn-paper collage, hand-drawn infographics, and 3D clay collaborator figures.
- Image provenance: every run records image source, model path, or local typography/composition method. Do not claim a model without verifiable evidence.
- Publishing pipeline: adds `build_wechat_publish_ready.py` and `submit_wechat_draft.sh`.
- Content confirmation: title, summary, cover, images, names, QR codes, secrets, and comment settings must be checked before draft submission.
- Parallel publishing: after article and images are confirmed, run a WeChat Draft Agent and Xiaohongshu Post Agent in parallel.
- Token-saving handoff: parallel subagents read only `publish-ready.md`, image manifests, and `content-pack.json`, not the full transcript.
- Cross-platform handoff: every run outputs `social-pack/content-pack.json` and `xiaohongshu/post.md` for Xiaohongshu and X reuse.
- Installation adapters: adds `installation.md` for Codex, Cursor, Cola, Claude, and generic `AGENTS.md` loading; Cola supports direct custom Skill package import.
- Documentation: all Markdown docs in the Skill package are bilingual Chinese/English for Chinese teams and future English-speaking reviewers.

### Core Deliverables

- `plan.md`: execution plan.
- `highlight-candidates.md`: candidate highlights.
- `highlight-scorecard.md`: highlight scoring.
- `platform-highlight-signals.md`: platform highlight signals.
- `evidence-map.md`: evidence map.
- `article-source.md`: source draft.
- `article-publish.md`: WeChat publish draft.
- `image-plan.md`: image plan.
- `image-prompts.md`: WeChat/Xiaohongshu image prompt pack.
- `style-reference-notes.md`: reference-image learning notes.
- `wechat/publish-ready.md`: WeChat API-ready markdown.
- `wechat/draft-submit-report.md`: draft submission report.
- `xiaohongshu/post.md`: Xiaohongshu post draft.
- `xiaohongshu/card-sequence.md`: Xiaohongshu card order.
- `social-pack/content-pack.json`: cross-platform content pack.
- `references/installation.md`: multi-platform installation guide.

### Non-Goals

- Do not automatically mass-send WeChat articles unless the user explicitly asks.
- Do not generate or redraw QR codes.
- Do not invent company names, metrics, links, or sensitive identities.
- Do not assume every platform has a native Skill registry. Platforms without native Skill support should load the package through Rules, project instructions, or `AGENTS.md`.
- Do not assume Xiaohongshu auto-publish is available unless a publishing tool or login state exists.

### Future X Skill Extension

A future `publish-to-x-from-content-pack` Skill can read `social-pack/content-pack.json` and:

1. Use the strongest hook as Post 1.
2. Compress WeChat chapters into a 6-10 post thread.
3. Keep image groups within 4 images per post.
4. Generate alt text for every image.
5. Prefer article links over QR-heavy images.
6. Output `x/thread.md`, `x/assets.json`, and a publish report.
