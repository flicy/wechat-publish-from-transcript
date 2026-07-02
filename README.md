# WeChat Publish From Transcript / 逐字稿到公众号发布

## 中文

`wechat-publish-from-transcript` 是一个 Agent Skill / workflow package，用于把访谈、直播、会议、视频或播客逐字稿加工成微信公众号发布稿，并同时生成配图 Prompt、小红书内容帖和跨平台内容包。

它不是单篇文章模板，而是一条发布链路：先从逐字稿提取高光，建立证据映射，再生成文章、图片计划、`wechat/publish-ready.md`、`social-pack/content-pack.json` 和发布检查报告。

### 适合场景

- 直播、圆桌、访谈、课程或会议复盘。
- 从逐字稿生成可发布的微信公众号文章。
- 同时准备小红书图文帖和 X/Twitter 线程素材。
- 需要图片 Prompt、图片尺寸规范、二维码安全合成和发布前检查。

### 快速安装

```bash
mkdir -p ~/.codex/skills
cp -R wechat-publish-from-transcript ~/.codex/skills/
```

也可以安装到项目内：

```bash
mkdir -p skills
cp -R wechat-publish-from-transcript skills/
```

### 微信草稿提交

公开版本不绑定任何个人、博主或私有发布器。需要创建微信草稿时，请配置本地 adapter：

```bash
export WECHAT_PUBLISHER_SCRIPT=/absolute/path/to/wechat-publisher-adapter
```

adapter 接口见 `references/wechat-publisher-adapter.md`。没有配置 adapter 时，`scripts/submit_wechat_draft.sh <run-dir> --dry-run` 仍会做本地轻量校验；真正提交草稿会要求先配置 adapter。

### 安全边界

- 二维码、Logo 和品牌资产必须使用用户提供的真实文件，不能由 AI 重绘。
- 不要把 AppSecret、Cookie、Token、二维码原图或私密 URL 写进公开仓库。
- 公开文档中不要引用个人发布器、个人账号或博主名称。
- 微信正式群发必须由用户单独明确授权。

### 主要输出

- `plan.md`
- `highlight-candidates.md`
- `highlight-scorecard.md`
- `evidence-map.md`
- `article-source.md`
- `article-publish.md`
- `image-plan.md`
- `image-prompts.md`
- `wechat/publish-ready.md`
- `wechat/preview-checklist.md`
- `wechat/draft-submit-report.md`
- `social-pack/content-pack.json`
- `xiaohongshu/post.md`

## English

`wechat-publish-from-transcript` is an Agent Skill / workflow package for turning transcripts from interviews, livestreams, meetings, videos, podcasts, or courses into WeChat Official Account articles, image prompts, Xiaohongshu posts, and reusable cross-platform content packs.

It is not a single article template. It is a publishing pipeline: extract transcript-based highlights, build an evidence map, draft the article, plan images, build `wechat/publish-ready.md`, generate `social-pack/content-pack.json`, and run publishing checks.

### Use Cases

- Recapping livestreams, roundtables, interviews, courses, or meetings.
- Turning a transcript into a publish-ready WeChat article.
- Preparing Xiaohongshu carousel posts and X/Twitter thread material.
- Producing image prompts, image size rules, QR-safe composition, and preflight checks.

### Quick Install

```bash
mkdir -p ~/.codex/skills
cp -R wechat-publish-from-transcript ~/.codex/skills/
```

Project-local install:

```bash
mkdir -p skills
cp -R wechat-publish-from-transcript skills/
```

### WeChat Draft Submission

The public package does not bind to any personal, blogger-specific, or private publisher. To create WeChat drafts, configure a local adapter:

```bash
export WECHAT_PUBLISHER_SCRIPT=/absolute/path/to/wechat-publisher-adapter
```

See `references/wechat-publisher-adapter.md` for the adapter contract. Without an adapter, `scripts/submit_wechat_draft.sh <run-dir> --dry-run` still performs a lightweight local check; actual draft creation requires the adapter.

### Safety Boundaries

- QR codes, logos, and brand assets must come from real user-provided files. Do not redraw them with AI.
- Do not commit AppSecret, cookies, tokens, QR source images, or private URLs to a public repository.
- Do not mention a personal publisher, personal account, or blogger name in public docs.
- Final WeChat mass-send/publish requires separate explicit user authorization.

### Main Outputs

- `plan.md`
- `highlight-candidates.md`
- `highlight-scorecard.md`
- `evidence-map.md`
- `article-source.md`
- `article-publish.md`
- `image-plan.md`
- `image-prompts.md`
- `wechat/publish-ready.md`
- `wechat/preview-checklist.md`
- `wechat/draft-submit-report.md`
- `social-pack/content-pack.json`
- `xiaohongshu/post.md`
