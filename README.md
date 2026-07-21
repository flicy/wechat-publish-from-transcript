# WeChat Publish From Transcript

> Turn a raw transcript into a WeChat Official Account article, image prompt pack, Xiaohongshu post, and reusable social content assets.

[中文](#中文) · [English](#english)

![Agent Skill](https://img.shields.io/badge/Agent-Skill-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![WeChat](https://img.shields.io/badge/WeChat-Draft-green)
![Bilingual Docs](https://img.shields.io/badge/Docs-ZH%20%2B%20EN-lightgrey)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

## 中文

`wechat-publish-from-transcript` 是一个公开可复用的 Agent Skill / workflow package。它接住一份访谈、直播、会议、课程、播客或视频逐字稿，把它加工成一整套发布资产，而不是只生成一篇文章。

一句话：给它逐字稿，它会先找证据和高光，再组织公众号文章、配图 Prompt、微信草稿输入稿、小红书内容帖和跨平台内容包。

### 它解决什么问题

很多内容复盘不是卡在“不会写”，而是卡在发布链路太散：

- 逐字稿很长，高光不知道怎么选。
- 公众号长文需要结构、证据、图片、标题、摘要和发布检查。
- 图片模型容易把中文标题做得过大，或把公众号横图做成小红书竖图。
- 二维码、Logo、品牌资产和私密凭证不能交给模型重绘或泄露。
- 同一场内容还要拆给小红书和 X/Twitter，不应该重新读一遍逐字稿。

这个 Skill 把这些步骤固定成一条可执行工作流。

### 一份逐字稿进来，它怎么接住

| 阶段 | 做什么 | 主要产物 |
| --- | --- | --- |
| 证据 | 从逐字稿抽取候选高光并评分 | `highlight-candidates.md`、`highlight-scorecard.md`、`evidence-map.md` |
| 写作 | 把高光组织成公众号长文 | `article-source.md`、`article-publish.md` |
| 配图 | 规划公众号横图和小红书竖图 | `image-plan.md`、`image-prompts.md` |
| 发布 | 生成微信草稿输入稿并做发布前检查 | `wechat/publish-ready.md`、`wechat/preview-checklist.md` |
| 分发 | 生成小红书和 X/Twitter 可复用内容 | `xiaohongshu/post.md`、`social-pack/content-pack.json` |

### 和普通写作提示词有什么不同

| 普通提示词 | 这个 Skill |
| --- | --- |
| 直接开始写文章 | 先抽高光、评分、建证据映射 |
| 观点可能来自模型补全 | 所有观点、案例、引用回到逐字稿证据 |
| 图片只是附带需求 | 图片比例、标题区、二维码和来源都有规则 |
| 只服务一个平台 | 同时沉淀微信、小红书和 X/Twitter 资产 |
| 发布靠人工记忆 | 有 dry-run、检查表和草稿提交适配器 |

### 核心能力

- **逐字稿高光筛选**：用 10 维评分表筛选可写、可传播、可图解的内容。
- **证据映射**：让文章观点、引用、案例能追溯回逐字稿。
- **公众号发布稿**：生成面向微信阅读场景的长文结构。
- **图片 Prompt 包**：输出统一母 Prompt 和逐图 Prompt。
- **图片安全边界**：二维码、Logo、品牌资产必须来自用户提供的真实文件。
- **微信草稿适配器**：公开包不绑定任何个人或私有发布器，通过本地 adapter 接入。
- **跨平台内容包**：生成小红书帖和 X/Twitter 可复用结构化数据。
- **公开发布检查**：内置脚本和 GitHub Actions 防止私有名称、本机路径和缓存文件回流。

### 快速开始

安装到 Codex：

```bash
mkdir -p ~/.codex/skills
cp -R wechat-publish-from-transcript ~/.codex/skills/
```

安装到项目内：

```bash
mkdir -p skills
cp -R wechat-publish-from-transcript skills/
```

触发示例：

```text
Use the wechat-publish-from-transcript Skill to turn this transcript into a WeChat article, image prompts, a WeChat draft payload, a Xiaohongshu post, and a social content pack.
```

中文示例：

```text
请使用 wechat-publish-from-transcript Skill，把这份逐字稿生成公众号发布稿、配图 Prompt、微信草稿和跨平台内容包。
```

### 微信草稿提交

公开版本不绑定任何个人、博主或私有发布器。需要创建微信草稿时，配置本地 adapter：

```bash
export WECHAT_PUBLISHER_SCRIPT=/absolute/path/to/wechat-publisher-adapter
```

adapter 接口：

```text
<publish-ready.md> --theme default [--dry-run]
```

没有配置 adapter 时，仍可做本地 dry-run：

```bash
scripts/submit_wechat_draft.sh outputs/<run-slug> --dry-run
```

完整接口见 `references/wechat-publisher-adapter.md`。

### 公开发布前检查

```bash
python3 scripts/check_public_ready.py .
bash -n scripts/submit_wechat_draft.sh
python3 -m unittest discover -s tests
```

如果在 Codex 环境中，也可以运行：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

### 安全边界

- 不用 AI 重绘二维码、Logo 或品牌资产。
- 不把 AppSecret、Cookie、Token、二维码原图或私密 URL 写入公开仓库。
- 不在公开文档中绑定个人发布器、个人账号或博主名称。
- 微信正式群发必须由用户单独明确授权。
- 图片来源、模型路径或本地合成方式必须记录；不能无依据声称使用了某个具体模型。

### 目录结构

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

## 相关 Skill

| Skill | 用途 |
|---|---|
| [enterprise-company-research-agent](https://github.com/flicy/enterprise-company-research-agent) | 企业供应商、公司与产品深度调研 |
| [prepare-livestream-event](https://github.com/flicy/prepare-livestream-event) | 筹备线上直播活动，生成海报、文案和发布清单 |
| [publish-skill-to-github](https://github.com/flicy/publish-skill-to-github) | 把本地 Skill 包发布到 GitHub |

## 许可证

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
<publish-ready.md> --theme default [--dry-run]
```

Without an adapter, local dry-run still works:

```bash
scripts/submit_wechat_draft.sh outputs/<run-slug> --dry-run
```

See `references/wechat-publisher-adapter.md` for the full contract.

### Public Readiness Checks

```bash
python3 scripts/check_public_ready.py .
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

## Related Skills

| Skill | Purpose |
|---|---|
| [enterprise-company-research-agent](https://github.com/flicy/enterprise-company-research-agent) | Enterprise supplier, company, and product research |
| [prepare-livestream-event](https://github.com/flicy/prepare-livestream-event) | Prepare livestream event launches with posters, copy, and publishing checklists |
| [publish-skill-to-github](https://github.com/flicy/publish-skill-to-github) | Publish local Skill packages to GitHub |

## License

MIT — see [LICENSE](./LICENSE)
