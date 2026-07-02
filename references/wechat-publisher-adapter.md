# WeChat Publisher Adapter / 微信发布适配器

## 中文

### 目的

公开发布本 Skill 时，不绑定任何个人、博主或私有发布器名称。微信草稿提交通过一个本地 adapter 接入，由使用者自行配置凭证、浏览器登录态或远程服务。

### 接口约定

`scripts/submit_wechat_draft.sh` 读取环境变量：

```bash
export WECHAT_PUBLISHER_SCRIPT=/absolute/path/to/wechat-publisher-adapter
```

adapter 必须接收以下参数：

```text
<publish-ready.md> --theme default [--dry-run]
```

其中：

- `<publish-ready.md>` 是 `wechat/publish-ready.md` 的绝对或相对路径。
- `--theme default` 表示使用默认公众号排版主题。
- `--dry-run` 表示只校验、渲染或预览，不创建草稿。

### 支持的 adapter 形式

`submit_wechat_draft.sh` 会按文件后缀选择运行方式：

| 后缀 | 运行方式 |
| --- | --- |
| `.ts` | `bun`，不可用时尝试 `npx -y bun` |
| `.js` / `.mjs` | `node` |
| `.py` | `python3` |
| 其他可执行文件 | 直接执行 |

### 未配置 adapter 时

如果没有设置 `WECHAT_PUBLISHER_SCRIPT`：

- `--dry-run` 会执行本地轻量校验，输出标题、作者、摘要、封面和正文图片数量。
- 非 dry-run 会失败，并提示用户配置本地 adapter。

### 安全要求

- 不要把 AppSecret、Cookie、Token、二维码原图或私密 URL 写入公开仓库。
- 不要在公开文档中出现个人发布器、个人账号或博主名称。
- 如果 adapter 使用微信 API，应由用户自己处理 IP 白名单。
- 如果 adapter 使用浏览器登录态，应由用户自己确认登录账号和草稿状态。

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
<publish-ready.md> --theme default [--dry-run]
```

Where:

- `<publish-ready.md>` is an absolute or relative path to `wechat/publish-ready.md`.
- `--theme default` requests the default WeChat article theme.
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
