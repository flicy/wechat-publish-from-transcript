# WeChat Draft Submission / 微信草稿提交

## 中文

### 原则

草稿提交是独立发布阶段：

1. 文章内容已经审阅。
2. 最终图片已经存在于本地。
3. 第一张公众号图片是 `2.35:1` 封面图：`assets/final/wechat/01-cover.png`。
4. `wechat/publish-ready.md` 包含真实本地图片引用。
5. API 提交前 dry-run 必须通过。
6. 用户明确要求提交或发布后，才允许创建草稿。
7. 草稿之后的正式群发/发布需要单独明确授权。
8. 草稿同步任务必须节省 token，只读取 `publish-ready.md`、图片清单和检查表，不重新读取完整逐字稿。
9. 发布器接口遵循 `references/wechat-publisher-adapter.md`，公开文档不得绑定个人或私有发布器名称。

### 必需输入

- `article-publish.md`
- `assets/final/wechat/01-cover.png`，比例 `2.35:1`
- `assets/final/wechat/00-overview-recap.png`
- `assets/final/wechat/` 下的章节图
- `wechat/preview-checklist.md`
- 已配置本地 WeChat publisher adapter
- adapter 可读取微信凭证或浏览器登录态

### 生成 `publish-ready.md`

优先使用脚本：

```bash
python3 <skill>/scripts/build_wechat_publish_ready.py \
  --run-dir outputs/<run-slug>
```

输出必须是：

```text
outputs/<run-slug>/wechat/publish-ready.md
```

正文图片引用必须相对 Markdown 文件，例如：

```md
![总回顾](../assets/final/wechat/00-overview-recap.png)
```

### 内容确认门

提交草稿前，更新 `wechat/preview-checklist.md` 并确认：

- 标题、摘要、作者、封面正确。
- 封面为 `2.35:1`，推荐尺寸 `1410 x 600` 或等比例。
- 文章标题块主色和封面/章节图主色一致，使用左侧主色条 + 浅色底截图式样。
- 嘉宾姓名、活动名称正确。
- 所有最终图片存在且对应文章段落。
- 图片文字无错字、超大标题、错名、假二维码、假 Logo 或虚构数据。
- 文章不包含私密凭证、手机号、私密链接或 AppSecret。
- 二维码如出现，必须是用户提供的真实文件。
- 评论设置已知。
- 发布方式默认为 `draft`，除非用户明确要求正式发布。

### Dry Run

先校验封面比例：

```bash
python3 <skill>/scripts/validate_assets.py \
  outputs/<run-slug>/assets/final/wechat/01-cover.png \
  --min-width 1000 \
  --min-height 400 \
  --ratio 2.35
```

```bash
<skill>/scripts/submit_wechat_draft.sh outputs/<run-slug> --dry-run
```

dry-run 应输出标题、作者、摘要、封面路径和正文图片数量。配置了 adapter 时，也可以输出 adapter 生成的 HTML 路径或预览路径。失败则不得提交。

### 创建草稿

```bash
<skill>/scripts/submit_wechat_draft.sh outputs/<run-slug>
```

脚本会调用 `WECHAT_PUBLISHER_SCRIPT` 指向的本地 adapter，通过微信草稿箱接口或浏览器登录态创建草稿。返回的 `media_id` 或草稿标识记录到：

```text
outputs/<run-slug>/wechat/draft-submit-report.md
```

## English

### Principle

Draft submission is a separate publishing stage:

1. The article has already been reviewed.
2. Final images already exist locally.
3. The first WeChat image is a `2.35:1` cover: `assets/final/wechat/01-cover.png`.
4. `wechat/publish-ready.md` contains real local image references.
5. Dry-run must pass before API submission.
6. Draft creation is allowed only after the user explicitly asks to submit or publish.
7. Final mass-send/publish beyond draft requires a separate explicit request.
8. The draft sync task must save tokens by reading only `publish-ready.md`, image manifests, and the checklist, not the full transcript.
9. The publisher interface follows `references/wechat-publisher-adapter.md`; public docs must not bind to a personal or private publisher name.

### Required Inputs

- `article-publish.md`
- `assets/final/wechat/01-cover.png` with `2.35:1` ratio
- `assets/final/wechat/00-overview-recap.png`
- Chapter images under `assets/final/wechat/`
- `wechat/preview-checklist.md`
- A local WeChat publisher adapter is configured
- WeChat credentials or browser login state are available to the adapter

### Build `publish-ready.md`

Prefer the helper:

```bash
python3 <skill>/scripts/build_wechat_publish_ready.py \
  --run-dir outputs/<run-slug>
```

The output must be:

```text
outputs/<run-slug>/wechat/publish-ready.md
```

Inline image references must be relative to the Markdown file.

### Content Confirmation Gate

Before draft submission, update `wechat/preview-checklist.md` and confirm:

- Title, summary, author, and cover are correct.
- Cover is `2.35:1`, recommended `1410 x 600` or equivalent.
- Article title block accent color matches the cover/chapter image accent color, using a left accent bar plus pale background.
- Speaker names and event names are correct.
- All final images exist and match the article sections.
- Image text has no typo, oversized title, wrong name, fake QR code, fake logo, or invented data.
- Article has no private credentials, phone number, private URL, or AppSecret.
- QR codes, if present, are real user-provided files.
- Comment settings are known.
- Publish mode is `draft` unless the user explicitly asks for final publish.

### Dry Run

Validate cover ratio first:

```bash
python3 <skill>/scripts/validate_assets.py \
  outputs/<run-slug>/assets/final/wechat/01-cover.png \
  --min-width 1000 \
  --min-height 400 \
  --ratio 2.35
```

```bash
<skill>/scripts/submit_wechat_draft.sh outputs/<run-slug> --dry-run
```

The dry-run should report title, author, digest, cover path, and inline image count. If an adapter is configured, it may also report a generated HTML path or preview path. Do not submit if dry-run fails.

### Create Draft

```bash
<skill>/scripts/submit_wechat_draft.sh outputs/<run-slug>
```

The wrapper calls the local adapter pointed to by `WECHAT_PUBLISHER_SCRIPT` and creates a draft through WeChat's draft API or browser-authenticated flow. Record the returned `media_id` or draft identifier in `outputs/<run-slug>/wechat/draft-submit-report.md`.

## 失败处理 / Failure Handling

- Missing publisher adapter / 缺少发布适配器：设置 `WECHAT_PUBLISHER_SCRIPT`，指向本机可用的微信草稿提交脚本。
- Missing credentials / 缺少凭证：按本地 adapter 要求配置微信凭证或浏览器登录态。
- IP allowlist failure / IP 白名单失败：使用 remote API 或让用户更新白名单。
- Image upload failure / 图片上传失败：校验图片路径和大小后重跑。
- Text or image issue after draft creation / 草稿创建后发现问题：修复后创建新草稿，不要静默修改正式发布。
