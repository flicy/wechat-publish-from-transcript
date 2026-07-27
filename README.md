# WeChat Publish From Transcript

> Turn a raw transcript into a WeChat Official Account article, image prompt pack, Xiaohongshu post, and reusable social content assets.

[中文](#中文) · [English](#english)

![Agent Skill](https://img.shields.io/badge/Agent-Skill-orange)![Python](https://img.shields.io/badge/Python-3.x-blue)![WeChat](https://img.shields.io/badge/WeChat-Draft-green)![Bilingual Docs](https://img.shields.io/badge/Docs-ZH%20%2B%20EN-lightgrey)[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

## 中文

`wechat-publish-from-transcript` 是一个面向内容运营的 Agent Skill / workflow 包。它把一场直播、访谈、会议、课程、播客或视频的原始转写稿，变成一套完整的发布资产，而不是只写一篇文章。

一句话：给它一份转写稿，它先找证据和亮点，再构建微信文章、图片 Prompt、微信草稿载荷、小红书帖子和可复用的跨平台社交资产。

### 它解决什么问题

转写稿整理工作通常不会因为"不会写"而失败，而是因为发布链条太散：

- 转写稿很长，最强的亮点不清楚。
- 微信文章需要结构、证据、图片、标题、摘要和预检检查。
- 图片模型可能 oversized 中文标题或创建竖版小红书风格图片给微信。
- 二维码、Logo、品牌资产和私密凭证不能被重绘或泄露。
- 同一场活动也需要小红书和 X/Twitter 资产而不重读整篇转写稿。

这个 Skill 把这些步骤变成一个可执行工作流。

### 一份转写稿进来后发生什么

| 阶段 | 它做什么 | 主要输出 |
| --- | --- | --- |
| 证据 | 提取和评分转写稿基础亮点 | `highlight-candidates.md`、`highlight-scorecard.md`、`evidence-map.md` |
| 写作 | 把亮点结构化成微信长文 | `article-source.md`、`article-publish.md` |
| 图片 | 规划微信横图和小红书竖版卡片 | `image-plan.md`、`image-prompts.md` |
| 排版 | 把文章排成可直接粘贴的公众号 HTML（主题 + 双关卡校验） | `wechat/article.html` |
| 发布 | 构建微信草稿载荷和预检清单 | `wechat/publish-ready.md`、`wechat/preview-checklist.md` |
| 分发 | 生成小红书和 X/Twitter 可复用内容 | `xiaohongshu/post.md`、`social-pack/content-pack.json` |

### 它和写作 Prompt 有什么不同

| 普通 Prompt | 这个 Skill |
| --- | --- |
| 立刻开始起草 | 先提取亮点、评分、建立证据 |
| 可能依赖模型补全 | 把主张、引用和例子扎根在转写稿证据 |
| 把图片当作附加项 | 定义图片比例、标题区、二维码规则和出处 |
| 只服务一个平台 | 产出微信、小红书和 X/Twitter 资产 |
| 把发布留给记忆 | 使用 dry-run 检查、清单和草稿适配器 |

### 核心能力

- **转写稿亮点选择**：使用 10 维评分卡找到值得写、值得分享、值得可视化的内容。
- **证据映射**：把文章主张、引用和例子追溯到转写稿。
- **微信文章起草**：为微信阅读行为构建长文。
- **图片 Prompt 包**：输出主 Prompt 和每图 Prompt。
- **图片安全边界**：二维码、Logo 和品牌资产必须来自真实用户提供的文件。
- **微信草稿适配器**：公开包不绑定个人或私密发布者。
- **公众号正文排版**：把 `article-publish.md` 排成可直接粘贴的公众号 HTML——扁平 `<section>` + 内联样式 + 中文 `<span leaf="">` 包裹，主题系统（默认增长橙）+ 双关卡校验。方法论改编自 [gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)（MIT）。
- **跨平台内容包**：生成小红书帖子材料和可复用 X/Twitter 结构。
- **公开就绪检查**：包含脚本和 GitHub Actions 来防止私密名字、本地路径和垃圾文件进入。

### 快速开始

为 Codex 安装：

```bash
mkdir -p ~/.codex/skills
cp -R wechat-publish-from-transcript ~/.codex/skills/
```

项目本地安装：

```bash
mkdir -p skills
cp -R wechat-publish-from-transcript skills/
```

触发例子：

```text
Use the wechat-publish-from-transcript Skill to turn this transcript into a WeChat article, image prompts, a WeChat draft payload, a Xiaohongshu post, and a social content pack.
```

中文触发：

```text
使用 wechat-publish-from-transcript Skill，把这份转写稿做成微信文章、图片 Prompt、微信草稿载荷、小红书帖子和社交内容包。
```

### 微信草稿提交

公开版本不绑定任何个人、博主专属或私密发布者。要创建微信草稿，需配置本地适配器：

```bash
export WECHAT_PUBLISHER_SCRIPT=/absolute/path/to/wechat-publisher-adapter
```

adapter 接口：

```text
<publish-ready.md> --theme default [--html <article.html>] [--dry-run]
```

如果没有 adapter，本地 dry-run 仍可工作：

```bash
scripts/submit_wechat_draft.sh outputs/<run-slug> --dry-run
```

完整契约见 `references/wechat-publisher-adapter.md`。

### 公众号正文排版

公众号编辑器不接受 Markdown，而且会剥离 `<style>`/`<div>`/`class`/CSS 变量等几乎所有样式手段。本 Skill 内置排版层（方法论改编自 [gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)，MIT），把 `article-publish.md` 排成可直接粘贴的 HTML：

- **输出形态**：扁平 `<section>` 嵌套 + 100% 内联样式，每段中文用 `<span leaf="">` 包裹（公众号粘贴解析器保留样式的钥匙）。
- **主题系统**：默认 `growth-orange`（增长橙，`#E6532E`），为逐字稿文章设计了讲者引用块、关键洞察框、章节序号、数据卡片等组件。见 `references/theme-index.md` / `references/theme-growth-orange.md`。
- **双关卡校验**：`scripts/validate_gzh_html.py`（动态，排版后必跑，0 ERROR 才交付）+ `scripts/component_lint.py`（静态，把关组件库）。
- **预览**：`scripts/wrap_preview.py` 把合规片段包成带「复制到公众号」按钮的浏览器页，一键复制粘贴。

```bash
python3 scripts/validate_gzh_html.py wechat/article.html   # 0 ERROR 才交付
python3 scripts/wrap_preview.py wechat/article.html         # 生成预览页
```

详见 `references/typeset-wechat-html.md`。

### 公开就绪检查

```bash
python3 scripts/check_public_ready.py .
python3 scripts/component_lint.py
bash -n scripts/submit_wechat_draft.sh
python3 -m unittest discover -s tests
```

在 Codex 环境中，也可以运行：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

### 安全边界

- 不要用 AI 重绘二维码、Logo 或品牌资产。
- 不要提交 AppSecret、cookie、token、二维码源图片或私密 URL 到公开仓库。
- 不要把公开文档绑定到个人发布者、个人账户或博主名字。
- 最终微信群发或发布需要单独明确用户授权。
- 记录图片来源、模型路径或本地合成方法。不要在没有可验证证据时声称模型。

### 仓库布局

```text
wechat-publish-from-transcript/
├── SKILL.md
├── README.md
├── PUBLISHING.md
├── LICENSE
├── skill.yml
├── agents/
├── assets/
├── references/
├── scripts/
└── tests/
```

### 相关 Skill

| Skill | 用途 |
|---|---|
| [enterprise-company-research-agent](https://github.com/flicy/enterprise-company-research-agent) | 企业供应商、公司和产品研究 |
| [prepare-livestream-event](https://github.com/flicy/prepare-livestream-event) | 准备直播活动发布，含海报、文案和发布清单 |
| [publish-skill-to-github](https://github.com/flicy/publish-skill-to-github) | 发布本地 Skill 包到 GitHub |

## 许可

MIT — 见 [LICENSE](./LICENSE)

## English

`wechat-publish-from-transcript` is a public, reusable Agent Skill / workflow package. It takes a transcript from an interview, livestream, meeting, course, podcast, or video and turns it into a complete publishing asset set, not just a single article.

In one sentence: give it a transcript, and it first finds evidence and highlights, then builds a WeChat article, image prompts, a WeChat draft payload, a Xiaohongshu post, and reusable cross-platform social assets.

### What Problem It Solves

Transcript recap work usually does not fail because writing is impossible. It fails because the publishing chain is scattered:

- The transcript is long, and the strongest highlights are unclear.
- A WeChat article needs structure, evidence, images, title, digest, and preflight checks.
- Image models may oversize Chinese headlines or create vertical Xiaohongshu-style images for WeChat.
- QR codes, logos, brand assets, and private credentials must not be redrawn or leaked.
- The same source event also needs Xiaohongshu and X/Twitter assets without rereading the whole transcript.

This Skill turns those steps into an executable workflow.

### What Happens After A Transcript Arrives

| Stage | What It Does | Main Outputs |
| --- | --- | --- |
| Evidence | Extract and score transcript-based highlights | `highlight-candidates.md`, `highlight-scorecard.md`, `evidence-map.md` |
| Writing | Structure the highlights into a WeChat longform article | `article-source.md`, `article-publish.md` |
| Images | Plan WeChat landscape images and Xiaohongshu vertical cards | `image-plan.md`, `image-prompts.md` |
| Typesetting | Render the article into paste-ready WeChat HTML (theme + dual-gate validation) | `wechat/article.html` |
| Publishing | Build the WeChat draft payload and preflight checklist | `wechat/publish-ready.md`, `wechat/preview-checklist.md` |
| Distribution | Generate Xiaohongshu and X/Twitter reusable content | `xiaohongshu/post.md`, `social-pack/content-pack.json` |

### How It Differs From A Writing Prompt

| A Normal Prompt | This Skill |
| --- | --- |
| Starts drafting immediately | Extracts highlights, scores them, and builds evidence first |
| May rely on model completion | Grounds claims, quotes, and examples in transcript evidence |
| Treats images as an add-on | Defines image ratios, title zones, QR rules, and provenance |
| Serves one platform | Produces WeChat, Xiaohongshu, and X/Twitter assets |
| Leaves publishing to memory | Uses dry-run checks, checklists, and a draft adapter |

### Core Capabilities

- **Transcript highlight selection**: uses a 10-dimension scorecard to find content worth writing, sharing, and visualizing.
- **Evidence mapping**: traces article claims, quotes, and examples back to the transcript.
- **WeChat article drafting**: builds a longform article for WeChat reading behavior.
- **Image prompt pack**: outputs a master prompt and per-image prompts.
- **Image safety boundaries**: QR codes, logos, and brand assets must come from real user-provided files.
- **WeChat draft adapter**: the public package does not bind to a personal or private publisher.
- **WeChat body typesetting**: renders `article-publish.md` into paste-ready WeChat HTML — flat `<section>` + inline styles + Chinese wrapped in `<span leaf="">`, a theme system (default Growth Orange) + dual-gate validation. Methodology adapted from [gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) (MIT).
- **Cross-platform content pack**: generates Xiaohongshu post material and reusable X/Twitter structure.
- **Public readiness checks**: includes scripts and GitHub Actions to prevent private names, local paths, and junk files from returning.

### Quick Start

Install for Codex:

```bash
mkdir -p ~/.codex/skills
cp -R wechat-publish-from-transcript ~/.codex/skills/
```

Project-local install:

```bash
mkdir -p skills
cp -R wechat-publish-from-transcript skills/
```

Trigger example:

```text
Use the wechat-publish-from-transcript Skill to turn this transcript into a WeChat article, image prompts, a WeChat draft payload, a Xiaohongshu post, and a social content pack.
```

### WeChat Draft Submission

The public version does not bind to any personal, blogger-specific, or private publisher. To create WeChat drafts, configure a local adapter:

```bash
export WECHAT_PUBLISHER_SCRIPT=/absolute/path/to/wechat-publisher-adapter
```

Adapter interface:

```text
<publish-ready.md> --theme default [--html <article.html>] [--dry-run]
```

Without an adapter, local dry-run still works:

```bash
scripts/submit_wechat_draft.sh outputs/<run-slug> --dry-run
```

See `references/wechat-publisher-adapter.md` for the full contract.

### WeChat Body Typesetting

The WeChat editor does not accept Markdown and strips almost every styling mechanism (`<style>`, `<div>`, `class`, CSS variables). This skill ships a typesetting layer (methodology adapted from [gzh-design-skill](https://github.com/isjiamu/gzh-design-skill), MIT) that renders `article-publish.md` into paste-ready HTML:

- **Output shape**: flat `<section>` nesting + 100% inline styles, every Chinese run wrapped in `<span leaf="">` (the attribute WeChat's paste parser preserves).
- **Theme system**: default `growth-orange` (`#E6532E`), with components built for transcript articles — speaker quote blocks, key-insight callouts, numbered chapter headings, data cards. See `references/theme-index.md` / `references/theme-growth-orange.md`.
- **Dual-gate validation**: `scripts/validate_gzh_html.py` (dynamic, mandatory after typesetting, 0 ERROR to ship) + `scripts/component_lint.py` (static, gates the component libraries).
- **Preview**: `scripts/wrap_preview.py` wraps a compliant fragment into a browser page with a copy-to-WeChat button.

```bash
python3 scripts/validate_gzh_html.py wechat/article.html   # 0 ERROR to ship
python3 scripts/wrap_preview.py wechat/article.html         # build preview page
```

See `references/typeset-wechat-html.md`.

### Public Readiness Checks

```bash
python3 scripts/check_public_ready.py .
python3 scripts/component_lint.py
bash -n scripts/submit_wechat_draft.sh
python3 -m unittest discover -s tests
```

In Codex environments, you can also run:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

### Safety Boundaries

- Do not redraw QR codes, logos, or brand assets with AI.
- Do not commit AppSecret, cookies, tokens, QR source images, or private URLs to a public repository.
- Do not bind public docs to a personal publisher, personal account, or blogger name.
- Final WeChat mass-send or publish requires separate explicit user authorization.
- Record image source, model path, or local composition method. Do not claim a model without verifiable evidence.

### Repository Layout

```text
wechat-publish-from-transcript/
├── SKILL.md
├── README.md
├── PUBLISHING.md
├── LICENSE
├── skill.yml
├── agents/
├── assets/
├── references/
├── scripts/
└── tests/
```

### Related Skills

| Skill | Purpose |
|---|---|
| [enterprise-company-research-agent](https://github.com/flicy/enterprise-company-research-agent) | Enterprise supplier, company, and product research |
| [prepare-livestream-event](https://github.com/flicy/prepare-livestream-event) | Prepare livestream event launches with posters, copy, and publishing checklists |
| [publish-skill-to-github](https://github.com/flicy/publish-skill-to-github) | Publish local Skill packages to GitHub |

## License

MIT — see [LICENSE](./LICENSE)
