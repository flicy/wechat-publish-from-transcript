# Input Contract / 输入契约

## 中文

### 必需输入

唯一必需输入是逐字稿。可接受形式：

- `.txt`
- `.md`
- 粘贴文本
- Notion 页面内容
- 视频转录结果

如果逐字稿带时间戳，必须保留。没有时间戳也继续提取高光，但在输出里标记为 `missing_timestamp`。

### 可选输入

- Notion 页面 URL 或导出的 Markdown
- 已有文章草稿
- 原始视频
- 微信/视频平台高光截图或数据截图
- 微信公众号关注二维码
- 社群二维码
- 微信 AppID/AppSecret 或已配置凭证
- 封面图
- 图片风格参考
- 用户偏好的公众号/小红书参考图
- 活动名称、期数、嘉宾简介
- GrowthOS 社群说明
- 小红书或 X 分发偏好

### 输入处理规则

1. 默认不要要求用户手工提供高光时刻。
2. 先从逐字稿生成候选高光。
3. 平台高光截图只作为验证信号，不作为独立事实来源。
4. 引用、观点和文章结构必须回到逐字稿找证据。
5. 如果没有视频，继续执行，并记录未做视觉/时间码核验。
6. 不要把 AppSecret 等密钥写入文章、SOP、报告或公开输出。

## English

### Required Input

The transcript is the only required content input. Accepted forms:

- `.txt`
- `.md`
- pasted text
- Notion page content
- video transcription result

If timestamps exist, preserve them. If not, continue highlight extraction and mark timestamps as `missing_timestamp`.

### Optional Inputs

- Notion page URL or exported Markdown
- Existing article draft
- Original video
- WeChat/video platform highlight screenshots or analytics screenshots
- WeChat Official Account QR code
- Community QR code
- WeChat AppID/AppSecret or existing configured credentials
- Cover image
- Image style references
- User-preferred WeChat/Xiaohongshu reference images
- Event name, issue number, speaker bios
- GrowthOS community description
- Xiaohongshu or X distribution preference

### Input Handling Rules

1. Do not ask the user to manually provide highlights by default.
2. Generate candidate highlights from the transcript first.
3. Treat platform highlight screenshots as validation signals, not standalone truth.
4. Use transcript evidence for quotes, claims, and article structure.
5. If video is unavailable, continue and record that visual/timecode verification was not performed.
6. Never write secrets such as AppSecret into article files, SOP files, reports, or public outputs.

## 输出目录 / Output Workspace

```text
outputs/<slug>/
├── plan.md
├── highlight-candidates.md
├── highlight-scorecard.md
├── platform-highlight-signals.md
├── evidence-map.md
├── article-source.md
├── article-publish.md
├── image-plan.md
├── image-prompts.md
├── style-reference-notes.md
├── assets/
├── wechat/
│   ├── preview-checklist.md
│   ├── publish-ready.md
│   └── draft-submit-report.md
├── xiaohongshu/
│   ├── post.md
│   └── card-sequence.md
└── social-pack/
    └── content-pack.json
```
