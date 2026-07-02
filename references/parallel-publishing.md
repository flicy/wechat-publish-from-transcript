# Parallel Publishing Workflow / 并行发布工作流

## 中文

### 目标

文章、图片和证据确认后，启动两个同步 Agent 任务：

1. `WeChat Draft Agent`：生成公众号草稿内容，使用节省 token 的方式同步到微信公众号草稿箱。
2. `Xiaohongshu Post Agent`：同步生成小红书帖子内容和图文笔记结构。

两个任务必须复用同一套上游资产，不重新读取完整逐字稿。

### 触发条件

只有当以下文件已经存在时，才能并行：

- `article-publish.md`
- `image-prompts.md`
- `assets/final/wechat/01-cover.png`
- `assets/final/wechat/00-overview-recap.png`
- `assets/final/wechat/` 下的正文图
- `social-pack/content-pack.json`
- `wechat/preview-checklist.md`

### Token 节省策略

并行子任务不要吃完整逐字稿。只传递最小上下文：

```text
WeChat Draft Agent:
- wechat/publish-ready.md
- assets/final/wechat/manifest.md 或图片路径清单
- wechat/preview-checklist.md
- 用户明确的提交/草稿要求

Xiaohongshu Post Agent:
- social-pack/content-pack.json
- image-plan.md
- image-prompts.md
- assets/final/xiaohongshu/ 图片路径清单
- CTA/二维码使用规则
```

父任务负责在并行前完成证据抽取、文章写作和图片规划。子任务只做平台装配和提交，不再要求模型重新总结逐字稿。

### WeChat Draft Agent

职责：

1. 确认公众号封面为第一张图，路径为 `assets/final/wechat/01-cover.png`。
2. 确认封面比例为 `2.35:1`，推荐尺寸 `1410 x 600` 或等比例。
3. 确认正文图为横版 16:9 或近似 16:9。
4. 确认公众号标题区主色和图片主色一致。
5. 运行：

```bash
python3 <skill>/scripts/build_wechat_publish_ready.py --run-dir outputs/<run-slug>
<skill>/scripts/submit_wechat_draft.sh outputs/<run-slug> --dry-run
```

6. 用户明确要求提交草稿后运行：

```bash
<skill>/scripts/submit_wechat_draft.sh outputs/<run-slug>
```

7. 把返回的 `media_id` 写入 `wechat/draft-submit-report.md`。

### Xiaohongshu Post Agent

职责：

1. 从 `social-pack/content-pack.json` 生成小红书帖子，不重新读取逐字稿。
2. 输出 `xiaohongshu/post.md`。
3. 输出或更新 `xiaohongshu/card-sequence.md`，说明 5-7 张图的顺序。
4. 标题使用最强钩子，正文保留短段落、清单和 CTA。
5. 如使用二维码，只能引用真实文件；默认不把二维码放在小红书首图。

优先使用脚本：

```bash
python3 <skill>/scripts/build_xiaohongshu_post.py \
  --content-pack outputs/<run-slug>/social-pack/content-pack.json \
  --out outputs/<run-slug>/xiaohongshu/post.md
```

### 汇总回报

父任务最后汇总：

- 微信草稿状态：dry-run / draft created / failed
- `media_id` 或失败原因
- 小红书帖子路径
- 小红书图卡路径
- 仍需人工确认的内容

## English

### Goal

After article, images, and evidence are confirmed, launch two parallel agent tasks:

1. `WeChat Draft Agent`: build the WeChat draft payload and sync it to the WeChat draft box with a token-efficient path.
2. `Xiaohongshu Post Agent`: generate the Xiaohongshu post copy and note structure in parallel.

Both tasks must reuse the same upstream assets. They must not re-read the full transcript.

### Preconditions

Parallel execution starts only after these files exist:

- `article-publish.md`
- `image-prompts.md`
- `assets/final/wechat/01-cover.png`
- `assets/final/wechat/00-overview-recap.png`
- WeChat inline images under `assets/final/wechat/`
- `social-pack/content-pack.json`
- `wechat/preview-checklist.md`

### Token-Saving Strategy

Parallel subagents must receive only minimal context:

```text
WeChat Draft Agent:
- wechat/publish-ready.md
- assets/final/wechat/manifest.md or image path list
- wechat/preview-checklist.md
- explicit user request for draft/submission

Xiaohongshu Post Agent:
- social-pack/content-pack.json
- image-plan.md
- image-prompts.md
- assets/final/xiaohongshu/ image path list
- CTA/QR rules
```

The parent task owns evidence extraction, article writing, and image planning before parallelization. Subagents only assemble platform outputs and submit drafts.

### WeChat Draft Agent

Responsibilities:

1. Confirm the WeChat cover is the first image at `assets/final/wechat/01-cover.png`.
2. Confirm cover ratio `2.35:1`, recommended `1410 x 600` or equivalent.
3. Confirm inline WeChat images are landscape 16:9 or near-16:9.
4. Confirm the WeChat article title accent color matches the dominant image accent color.
5. Run:

```bash
python3 <skill>/scripts/build_wechat_publish_ready.py --run-dir outputs/<run-slug>
<skill>/scripts/submit_wechat_draft.sh outputs/<run-slug> --dry-run
```

6. After explicit user request, run:

```bash
<skill>/scripts/submit_wechat_draft.sh outputs/<run-slug>
```

7. Record the returned `media_id` in `wechat/draft-submit-report.md`.

### Xiaohongshu Post Agent

Responsibilities:

1. Generate Xiaohongshu post copy from `social-pack/content-pack.json` without re-reading the transcript.
2. Output `xiaohongshu/post.md`.
3. Output or update `xiaohongshu/card-sequence.md` for the 5-7 card order.
4. Use the strongest hook as the title; keep body paragraphs short with lists and CTA.
5. If QR codes are used, reference only real files. Do not use QR-heavy images as the first card by default.

Prefer the helper:

```bash
python3 <skill>/scripts/build_xiaohongshu_post.py \
  --content-pack outputs/<run-slug>/social-pack/content-pack.json \
  --out outputs/<run-slug>/xiaohongshu/post.md
```

### Final Report

The parent task reports:

- WeChat draft status: dry-run / draft created / failed
- `media_id` or failure reason
- Xiaohongshu post path
- Xiaohongshu card paths
- Remaining manual checks
