# Installation Guide / 安装说明

## 中文

### 适用平台

`wechat-publish-from-transcript` 是一套平台无关的 Agent Skill / workflow package。它可以在 Codex、Cursor、Cola、Claude 等开发或 Agent 平台中使用。

核心原则：只维护一份 Skill 包，不为每个平台复制逻辑。不同平台只做“加载入口”适配。

### 推荐目录结构

把完整 Skill 包放到项目或个人 Skill 目录：

```text
wechat-publish-from-transcript/
├── SKILL.md
├── references/
├── scripts/
├── assets/
└── agents/
```

不要只复制 `SKILL.md`。图片规范、安装说明、发布脚本和参考文档都在子目录里。

### Codex 安装

个人安装：

```bash
mkdir -p ~/.codex/skills
cp -R wechat-publish-from-transcript ~/.codex/skills/
```

如果你的 Codex 环境使用 `~/.agents/skills`：

```bash
mkdir -p ~/.agents/skills
cp -R wechat-publish-from-transcript ~/.agents/skills/
```

验证：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  ~/.codex/skills/wechat-publish-from-transcript
```

如果没有 `quick_validate.py`，至少检查 `SKILL.md`、`references/` 和 `scripts/` 是否完整存在。

### Claude / Claude Code 安装

个人安装：

```bash
mkdir -p ~/.claude/skills
cp -R wechat-publish-from-transcript ~/.claude/skills/
```

项目安装：

```bash
mkdir -p .claude/skills
cp -R wechat-publish-from-transcript .claude/skills/
```

在 Claude 中触发时说明：

```text
请使用 wechat-publish-from-transcript Skill，把这份逐字稿生成公众号发布稿、配图 Prompt、微信草稿和跨平台内容包。
```

### Cursor 安装

Cursor 通常通过项目 Rules 加载工作流。建议把 Skill 包放进项目：

```bash
mkdir -p skills
cp -R wechat-publish-from-transcript skills/
mkdir -p .cursor/rules
```

创建 `.cursor/rules/wechat-publish-from-transcript.mdc`：

```mdc
---
description: Use when turning a transcript, livestream, interview, meeting, video, or Notion page into a WeChat Official Account article and reusable Xiaohongshu/X assets.
alwaysApply: false
---

When the user asks to create or publish a WeChat Official Account article from a transcript, first read:

- skills/wechat-publish-from-transcript/SKILL.md
- skills/wechat-publish-from-transcript/references/input-contract.md
- skills/wechat-publish-from-transcript/references/highlight-selection.md
- skills/wechat-publish-from-transcript/references/image-style.md
- skills/wechat-publish-from-transcript/references/wechat-draft-submit.md

Follow the workflow in SKILL.md. Treat the transcript as the only required content input. Do not invent highlights or claims without transcript evidence.
```

### Cola 安装

Cola 支持自定义 Skill 包。推荐直接导入完整目录 `wechat-publish-from-transcript/`，并把 `SKILL.md` 设置为入口文件。

如果要随项目托管 Skill 包，也可以：

```bash
mkdir -p skills
cp -R wechat-publish-from-transcript skills/
```

然后在 Cola 的项目规则、`COLA.md` 或 `AGENTS.md` 中加入：

```markdown
## WeChat Publish From Transcript

When the user asks to create or publish a WeChat article from a transcript, read `skills/wechat-publish-from-transcript/SKILL.md` first and follow its referenced documents.
```

### 通用 AGENTS.md 适配

任何平台只要能读取项目文件，都可以通过 `AGENTS.md` 接入：

```markdown
## Transcript-to-WeChat Publishing

For transcript-to-WeChat tasks, use `skills/wechat-publish-from-transcript/SKILL.md`.

Required behavior:
- Generate highlights from the transcript before drafting.
- Score highlights with `references/highlight-selection.md`.
- Build article, image prompts, WeChat draft assets, and `social-pack/content-pack.json`.
- Use real QR/logo files only.
- Create a WeChat draft only after explicit user confirmation.
```

### 发布依赖

最小依赖：

- Python 3
- 可读写本地文件
- 可调用图片生成工具或用户提供成图

微信草稿提交依赖：

- 本地 WeChat publisher adapter
- `WECHAT_APP_ID`
- `WECHAT_APP_SECRET`
- 微信公众平台 IP 白名单，或可用的浏览器登录态

不要把 `WECHAT_APP_SECRET` 写进文档、截图、公开仓库或发布稿。优先使用环境变量或本机私密配置。

公开发布本 Skill 时，不要把个人、博主或私有发布器名称写进文档。通过环境变量接入本地发布器：

```bash
export WECHAT_PUBLISHER_SCRIPT=/absolute/path/to/wechat-publisher-adapter
```

adapter 接收参数：

```text
<publish-ready.md> --theme default [--dry-run]
```

### 安装后自检

检查：

```bash
test -f wechat-publish-from-transcript/SKILL.md
test -f wechat-publish-from-transcript/references/installation.md
test -f wechat-publish-from-transcript/references/image-style.md
test -f wechat-publish-from-transcript/references/wechat-publisher-adapter.md
test -f wechat-publish-from-transcript/scripts/build_wechat_publish_ready.py
test -f wechat-publish-from-transcript/scripts/submit_wechat_draft.sh
```

试运行建议：

1. 用一小段逐字稿生成 `highlight-candidates.md`。
2. 确认高光不是用户手工提供，而是从逐字稿生成。
3. 确认 `image-prompts.md` 包含统一母 Prompt 和逐图 Prompt。
4. 确认微信提交前会先生成 `wechat/publish-ready.md` 并 dry-run。

## English

### Supported Platforms

`wechat-publish-from-transcript` is a platform-neutral Agent Skill / workflow package. It can be used in Codex, Cursor, Cola, Claude, and similar coding-agent environments.

Core principle: maintain one Skill package and adapt only the loading entry point for each platform.

### Recommended Directory Layout

Keep the full Skill package together:

```text
wechat-publish-from-transcript/
├── SKILL.md
├── references/
├── scripts/
├── assets/
└── agents/
```

Do not copy `SKILL.md` alone. The image rules, installation notes, publishing scripts, and reference docs live in subdirectories.

### Codex Installation

Personal install:

```bash
mkdir -p ~/.codex/skills
cp -R wechat-publish-from-transcript ~/.codex/skills/
```

If your Codex environment uses `~/.agents/skills`:

```bash
mkdir -p ~/.agents/skills
cp -R wechat-publish-from-transcript ~/.agents/skills/
```

Validate:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  ~/.codex/skills/wechat-publish-from-transcript
```

If `quick_validate.py` is unavailable, at minimum confirm that `SKILL.md`, `references/`, and `scripts/` are present.

### Claude / Claude Code Installation

Personal install:

```bash
mkdir -p ~/.claude/skills
cp -R wechat-publish-from-transcript ~/.claude/skills/
```

Project install:

```bash
mkdir -p .claude/skills
cp -R wechat-publish-from-transcript .claude/skills/
```

Trigger prompt:

```text
Use the wechat-publish-from-transcript Skill to turn this transcript into a WeChat article, image prompts, WeChat draft, and cross-platform content pack.
```

### Cursor Installation

Cursor usually loads reusable workflows through project Rules. Put the Skill package in the project:

```bash
mkdir -p skills
cp -R wechat-publish-from-transcript skills/
mkdir -p .cursor/rules
```

Create `.cursor/rules/wechat-publish-from-transcript.mdc`:

```mdc
---
description: Use when turning a transcript, livestream, interview, meeting, video, or Notion page into a WeChat Official Account article and reusable Xiaohongshu/X assets.
alwaysApply: false
---

When the user asks to create or publish a WeChat Official Account article from a transcript, first read:

- skills/wechat-publish-from-transcript/SKILL.md
- skills/wechat-publish-from-transcript/references/input-contract.md
- skills/wechat-publish-from-transcript/references/highlight-selection.md
- skills/wechat-publish-from-transcript/references/image-style.md
- skills/wechat-publish-from-transcript/references/wechat-draft-submit.md

Follow the workflow in SKILL.md. Treat the transcript as the only required content input. Do not invent highlights or claims without transcript evidence.
```

### Cola Installation

Cola supports custom Skill packages. Prefer importing the full `wechat-publish-from-transcript/` directory and setting `SKILL.md` as the entry file.

If you want to keep the Skill package inside the project, use:

```bash
mkdir -p skills
cp -R wechat-publish-from-transcript skills/
```

Then add this to Cola project rules, `COLA.md`, or `AGENTS.md`:

```markdown
## WeChat Publish From Transcript

When the user asks to create or publish a WeChat article from a transcript, read `skills/wechat-publish-from-transcript/SKILL.md` first and follow its referenced documents.
```

### Generic AGENTS.md Adapter

Any platform that can read project files can load the Skill through `AGENTS.md`:

```markdown
## Transcript-to-WeChat Publishing

For transcript-to-WeChat tasks, use `skills/wechat-publish-from-transcript/SKILL.md`.

Required behavior:
- Generate highlights from the transcript before drafting.
- Score highlights with `references/highlight-selection.md`.
- Build article, image prompts, WeChat draft assets, and `social-pack/content-pack.json`.
- Use real QR/logo files only.
- Create a WeChat draft only after explicit user confirmation.
```

### Publishing Dependencies

Minimum dependencies:

- Python 3
- Local file read/write access
- An image generation tool or user-provided final images

WeChat draft submission dependencies:

- A local WeChat publisher adapter
- `WECHAT_APP_ID`
- `WECHAT_APP_SECRET`
- WeChat Official Account IP allowlist, or an available browser login state

Do not write `WECHAT_APP_SECRET` into docs, screenshots, public repos, or article drafts. Prefer environment variables or local secret storage.

When publishing this Skill publicly, do not reference a personal, blogger-specific, or private publisher by name. Connect the local publisher through an environment variable:

```bash
export WECHAT_PUBLISHER_SCRIPT=/absolute/path/to/wechat-publisher-adapter
```

The adapter receives:

```text
<publish-ready.md> --theme default [--dry-run]
```

### Post-Install Check

Check:

```bash
test -f wechat-publish-from-transcript/SKILL.md
test -f wechat-publish-from-transcript/references/installation.md
test -f wechat-publish-from-transcript/references/image-style.md
test -f wechat-publish-from-transcript/references/wechat-publisher-adapter.md
test -f wechat-publish-from-transcript/scripts/build_wechat_publish_ready.py
test -f wechat-publish-from-transcript/scripts/submit_wechat_draft.sh
```

Suggested smoke test:

1. Use a short transcript to generate `highlight-candidates.md`.
2. Confirm highlights are generated from the transcript, not manually supplied by the user.
3. Confirm `image-prompts.md` includes a master prompt and per-image prompts.
4. Confirm WeChat submission builds `wechat/publish-ready.md` and runs dry-run before any draft creation.
