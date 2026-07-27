# WeChat Publisher Adapter / 微信发布适配器

## 中文

### 目的

公开 Skill 包不能绑定任何个人、博主专属或私密发布者名字。微信草稿提交通过本地 adapter 连接，每个用户自己负责凭证、浏览器登录态或远程服务。

### 接口契约

`scripts/submit_wechat_draft.sh` 读取环境变量：

```bash
export WECHAT_PUBLISHER_SCRIPT=/absolute/path/to/wechat-publisher-adapter
```

adapter 必须接受：

```text
<publish-ready.md> --theme default [--html <article.html>] [--dry-run]
```

其中：

- `<publish-ready.md>` 是 `wechat/publish-ready.md` 的绝对或相对路径。
- `--theme default` 请求默认微信文章主题。
- `--html <article.html>` 可选：传入已排版并校验（0 ERROR）的正文 HTML（`wechat/article.html`）。提供时 adapter 直接用它作为正文，不再自行排版；不提供时由 adapter 自行排版 Markdown 或用平台默认。推荐始终传入。
- `--dry-run` 表示验证、渲染或预览，不创建草稿。

### 支持的 adapter 类型

`submit_wechat_draft.sh` 按文件扩展名选择运行器：

| 扩展名 | 运行器 |
| --- | --- |
| `.ts` | `bun`，如果不可用则 `npx -y bun` |
| `.js` / `.mjs` | `node` |
| `.py` | `python3` |
| 其他可执行文件 | 直接运行 |

### 没有 adapter 时

如果 `WECHAT_PUBLISHER_SCRIPT` 未设置：

- `--dry-run` 运行轻量本地检查，打印标题、作者、摘要、封面和内嵌图数量。
- 非 dry-run 失败并要求用户配置本地 adapter。

### 安全要求

- 不要提交 AppSecret、Cookie、Token、二维码源图片或私密 URL 到公开仓库。
- 不要在公开文档中提及个人发布者、个人账户或博主名字。
- 如果 adapter 使用微信 API，用户必须处理 IP 白名单。
- 如果 adapter 使用浏览器登录态，用户必须确认活跃账户和草稿状态。

## English

### Purpose

When this Skill is published publicly, it must not bind itself to any personal, blogger-specific, or private publisher name. WeChat draft submission is connected through a local adapter, and each user is responsible for credentials, browser login state, or remote services.

### Interface Contract

`scripts/submit_wechat_draft.sh` reads this environment variable:

```bash
export WECHAT_PUBLISHER_SCRIPT=/absolute/path/to/wechat-publisher-adapter
```

The adapter must accept:

```text
<publish-ready.md> --theme default [--html <article.html>] [--dry-run]
```

Where:

- `<publish-ready.md>` is an absolute or relative path to `wechat/publish-ready.md`.
- `--theme default` requests the default WeChat article theme.
- `--html <article.html>` optional: pass the already-typeset, validated (0 ERROR) body HTML (`wechat/article.html`). When present, the adapter uses it verbatim as the body and does not re-typeset; when absent, the adapter typesets the Markdown itself or falls back to the platform default. Always passing it is recommended.
- `--dry-run` means validate, render, or preview without creating a draft.

### Supported Adapter Types

`submit_wechat_draft.sh` chooses the runner by file extension:

| Extension | Runner |
| --- | --- |
| `.ts` | `bun`, falling back to `npx -y bun` |
| `.js` / `.mjs` | `node` |
| `.py` | `python3` |
| Other executable file | Run directly |

### Without an Adapter

If `WECHAT_PUBLISHER_SCRIPT` is not set:

- `--dry-run` runs a lightweight local check and prints title, author, digest, cover, and inline image count.
- Non-dry-run fails and asks the user to configure a local adapter.

### Safety Requirements

- Do not commit AppSecret, cookies, tokens, QR source images, or private URLs to a public repository.
- Do not mention a personal publisher, personal account, or blogger name in public docs.
- If the adapter uses the WeChat API, the user must handle IP allowlisting.
- If the adapter uses browser login state, the user must confirm the active account and draft status.
