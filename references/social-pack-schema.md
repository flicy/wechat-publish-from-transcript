# Social Pack Schema / 跨平台内容包结构

## 中文

每次运行都必须输出 `social-pack/content-pack.json`，让小红书和 X 工作流复用公众号阶段已经完成的工作，而不是重新读逐字稿。

### 用途

- 小红书图文：复用高光、标题、证据、卡片顺序和 CTA。
- X thread：复用最强钩子、线程结构、图片分组、alt text。
- 后续复盘：快速查看内容来源、评分、证据和发布链接。

### Schema

```json
{
  "title": "",
  "summary": "",
  "source_url": "",
  "wechat_url": "",
  "audience": "",
  "highlight_method": {
    "source": "transcript",
    "scoring_dimensions": [
      "hook",
      "information_density",
      "practical_value",
      "story",
      "novelty",
      "quoteability",
      "standalone_completeness",
      "visual_potential",
      "platform_interaction_signal",
      "risk_control"
    ]
  },
  "highlights": [
    {
      "id": "h01",
      "timestamp": "",
      "title": "",
      "score": 0,
      "reason": "",
      "platform_signals": [
        "most_online_viewers",
        "highest_comment_rate",
        "highest_retention_rate"
      ],
      "platform_source": "wechat_highlight_screenshot | video_analytics | none",
      "evidence_excerpt": "",
      "quote_candidates": [],
      "image_task": "pain_point | insight | method | workflow | case | summary"
    }
  ],
  "chapters": [
    {
      "id": "01",
      "title": "",
      "highlight_id": "h01",
      "hook": "",
      "key_points": [],
      "quotes": [],
      "timestamp": "",
      "image": "",
      "xhs_card": ""
    }
  ],
  "cta": {
    "wechat": "",
    "community": "",
    "qrcode_image": ""
  },
  "xiaohongshu": {
    "post_path": "xiaohongshu/post.md",
    "card_sequence_path": "xiaohongshu/card-sequence.md",
    "cards": [
      {
        "index": 1,
        "role": "cover | pain | insight | method | case | community | summary",
        "title": "",
        "image": ""
      }
    ]
  }
}
```

### X 扩展规则

- 第 1 条使用最强钩子高光。
- 单条 X 图片组通常控制在 4 张以内。
- 二维码重的图片不适合 X，优先使用文章链接。
- 每张图片都要写 alt text。
- 不把微信长文照搬成线程，要改成连续判断和证据链。

### 小红书扩展规则

- 标准笔记使用 5-7 张图。
- 封面承载最强钩子。
- 中间页跟随最终高光。
- 末页可以承载社群/活动 CTA；如需二维码，必须用真实文件合成。
- 小红书帖子生成必须优先读取 `social-pack/content-pack.json`，不要重新读取完整逐字稿。
- 默认输出 `xiaohongshu/post.md` 和 `xiaohongshu/card-sequence.md`。

## English

Every run must output `social-pack/content-pack.json` so Xiaohongshu and X workflows can reuse the work already completed for WeChat instead of re-reading the transcript.

### Purpose

- Xiaohongshu notes: reuse highlights, titles, evidence, card order, and CTA.
- X threads: reuse strongest hook, thread structure, image grouping, and alt text.
- Future review: quickly inspect source, score, evidence, and publish links.

### Schema

Use the JSON schema shown in the Chinese section above.

### X Extension Rules

- Use the strongest hook highlight for Post 1.
- X single-post image groups should usually stay within 4 images.
- QR-heavy images are less suitable for X; prefer article links.
- Always write alt text for images.
- Do not copy the WeChat longform directly. Rewrite as a sequence of judgments and evidence.

### Xiaohongshu Extension Rules

- Use 5-7 images for a standard note.
- The cover must carry the strongest hook.
- Middle cards should follow selected highlights.
- The last card may carry community/event CTA; if QR code is needed, compose it from a real file.
- Xiaohongshu post generation must read `social-pack/content-pack.json` first and must not re-read the full transcript by default.
- Default outputs are `xiaohongshu/post.md` and `xiaohongshu/card-sequence.md`.
