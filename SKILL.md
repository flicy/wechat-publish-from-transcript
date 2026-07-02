---
name: wechat-publish-from-transcript
description: Use when creating or publishing a 微信公众号 article from a talk, livestream, interview, meeting, video, transcript, or Notion page, especially when the task needs transcript-based highlights, evidence mapping, article drafting, Image 2.0/GPT Image prompt packs, reference-image style learning, QR-safe image planning, WeChat draft/publish execution, or reusable Xiaohongshu/X content packs.
---

# WeChat Publish From Transcript / 逐字稿到公众号发布

## 中文概览

这个 Skill 把一份原始逐字稿变成可发布的微信公众号文章，并同时沉淀小红书和 X 可复用的内容包。它是一套平台无关的 Agent Skill / workflow package，可通过 Codex、Cursor、Cola、Claude 等环境加载。它的边界不是“写一篇文章”，而是跑完一条发布链路：高光提取、证据映射、文章结构、配图计划、可复用 Prompt、最终图片、公众号草稿、并行小红书帖子、发布报告和跨平台资产。

## English Overview

This skill turns a raw transcript into a WeChat Official Account article and reusable Xiaohongshu/X assets. It is a platform-neutral Agent Skill / workflow package that can be loaded from Codex, Cursor, Cola, Claude, and similar environments. Its scope is not just article writing. It runs the full publishing pipeline: highlight extraction, evidence mapping, article structure, image planning, reusable prompts, final assets, WeChat draft submission, parallel Xiaohongshu post generation, publish reporting, and cross-platform handoff.

## 必须执行 / Required Behavior

1. 先创建计划。 / Start with a plan.
2. 把逐字稿视为唯一必需内容输入。 / Treat the transcript as the only required content input.
3. 写文章前先从逐字稿生成候选高光。 / Generate candidate highlights from the transcript before drafting.
4. 用 `references/highlight-selection.md` 的 10 维评分表筛选高光。 / Score highlights with the 10-dimension scorecard in `references/highlight-selection.md`.
5. 用最终高光组织文章章节和章节解释图。 / Use final highlights to structure chapters and chapter explanation images.
6. 所有观点、引用、案例都要能追溯到逐字稿证据。 / Support claims, quotes, and cases with transcript evidence.
7. 二维码、Logo、品牌资产必须使用用户提供的真实文件，不得让 AI 重绘。 / Use real user-provided QR codes, logos, and brand assets. Never regenerate them with AI.
8. 微信草稿或发布使用用户本地配置的 WeChat publisher adapter，不在公开 Skill 中绑定个人或私有发布器。 / Use the user's locally configured WeChat publisher adapter for draft or publish execution. Do not bind the public Skill to a personal or private publisher.
9. 必须加入一张 `00-overview-recap` 总回顾图。 / Always include one `00-overview-recap` whole-session recap image.
10. 必须输出 `image-prompts.md`，包含统一母 Prompt 和每张公众号/小红书图的可直接使用 Prompt。 / Output `image-prompts.md` with unified master prompts and per-image prompts for WeChat and Xiaohongshu.
11. 必须输出 `social-pack/content-pack.json`，给小红书和 X 复用。 / Output `social-pack/content-pack.json` for Xiaohongshu and X reuse.
12. 对所有图片记录来源、模型路径或本地合成方式、最终文件路径。除非模型路径可验证，不要声称用了某个具体模型。 / Record image provenance: source/model path, composition steps, and final paths. Do not claim a specific model unless verifiable.
13. 公众号第一张图必须是 `2.35:1` 封面图，默认路径 `assets/final/wechat/01-cover.png`。 / The first WeChat image must be a `2.35:1` cover at `assets/final/wechat/01-cover.png`.
14. 公众号文章标题的主色和图片主色必须一致，采用左侧强调色条/浅色底标题块的截图式样。 / Match the WeChat article title accent color with the image accent color, using a screenshot-like title block with a left accent bar and pale background.
15. 微信提交前必须生成 `wechat/publish-ready.md`，先 dry-run，再在用户明确要求提交/发布后创建草稿。 / For WeChat submission, build `wechat/publish-ready.md`, run a dry-run, then create a draft only after explicit user request.
16. 图片和文章确认后，启动两个同步任务：微信草稿 Agent 和小红书帖子 Agent；两个任务只接收最小上下文，不重新读取完整逐字稿。 / After article and image confirmation, launch two parallel tasks: WeChat Draft Agent and Xiaohongshu Post Agent. Both receive minimal context and must not re-read the full transcript.
17. 交付时必须说明输入、输出、图片来源、发布状态、限制，并询问是否需要修改。 / At handoff, report inputs, outputs, image provenance, publish status, limitations, and ask whether changes are needed.

## 工作流 / Workflow

1. 解析输入：`references/input-contract.md`。 / Resolve inputs with `references/input-contract.md`.
2. 创建 `plan.md`。 / Create `plan.md`.
3. 从逐字稿提取候选高光。 / Extract transcript-based highlight candidates.
4. 合并微信/视频平台高光截图信号。 / Merge optional WeChat/video platform highlight screenshot signals.
5. 建立 `evidence-map.md`。 / Build `evidence-map.md`.
6. 起草 `article-source.md`，再整理 `article-publish.md`。 / Draft `article-source.md`, then prepare `article-publish.md`.
7. 按最终高光规划图片，包括 `00-overview-recap`。 / Plan images from final highlights, including `00-overview-recap`.
8. 生成 `image-prompts.md`，结合文章、逐字稿、配图计划和参考图。 / Generate `image-prompts.md` from article, transcript, image plan, and reference images.
9. 生成或合成图片；二维码只做真实文件合成。 / Generate or compose images; compose QR codes only from real files.
10. 记录图片来源和排版方式。 / Record image provenance and typography/composition method.
11. 跑 `references/wechat-checklist.md` 的发布前检查。 / Run the preflight checklist in `references/wechat-checklist.md`.
12. 生成 `social-pack/content-pack.json`。 / Build `social-pack/content-pack.json`.
13. 用 `references/wechat-draft-submit.md` 生成 `publish-ready.md` 并 dry-run。 / Build `publish-ready.md` and dry-run via `references/wechat-draft-submit.md`.
14. 按 `references/parallel-publishing.md` 同步执行微信草稿任务和小红书帖子任务。 / Run WeChat draft and Xiaohongshu post tasks in parallel with `references/parallel-publishing.md`.
15. 用本地 WeChat publisher adapter 创建微信草稿或执行发布。 / Create a WeChat draft or publish through the local WeChat publisher adapter.
16. 输出路径、状态、限制和下一步。 / Report paths, status, limitations, and next steps.

## 何时读取参考文档 / When To Read References

- 输入不清楚：`references/input-contract.md`。 / Input ambiguity: `references/input-contract.md`.
- 高光提取和评分：`references/highlight-selection.md`。 / Highlight extraction and scoring: `references/highlight-selection.md`.
- 产品边界、迭代说明、未来 X 扩展：`references/product-notes.md`。 / Product boundaries, iteration notes, and X extension: `references/product-notes.md`.
- 安装到 Codex、Cursor、Cola、Claude 或通用 Agent 项目：`references/installation.md`。 / Installation for Codex, Cursor, Cola, Claude, or generic agent projects: `references/installation.md`.
- 配图、参考图学习、字号规范、二维码合成：`references/image-style.md`。 / Image prompts, style learning, typography rules, and QR handling: `references/image-style.md`.
- 发布前检查：`references/wechat-checklist.md`。 / Publishing readiness: `references/wechat-checklist.md`.
- 微信草稿提交：`references/wechat-draft-submit.md`。 / WeChat draft submission: `references/wechat-draft-submit.md`.
- 微信发布适配器接口：`references/wechat-publisher-adapter.md`。 / WeChat publisher adapter interface: `references/wechat-publisher-adapter.md`.
- 微信草稿和小红书帖子并行任务：`references/parallel-publishing.md`。 / Parallel WeChat draft and Xiaohongshu post tasks: `references/parallel-publishing.md`.
- 跨平台内容包：`references/social-pack-schema.md`。 / Cross-platform handoff: `references/social-pack-schema.md`.
- 完整 SOP：`references/sop.md`。 / Full SOP: `references/sop.md`.

## 脚本 / Script Helpers

- `scripts/extract_highlights.py`：生成启发式高光候选骨架。 / Heuristic highlight candidate scaffold.
- `scripts/build_content_pack.py`：从证据和文章生成 `content-pack.json` 初稿。 / Starter `content-pack.json` builder.
- `scripts/compose_qrcode_card.py`：把真实二维码合成到图卡。 / Compose real QR codes onto image cards.
- `scripts/validate_assets.py`：检查图片尺寸和缺失文件。 / Validate image dimensions and missing files.
- `scripts/build_wechat_publish_ready.py`：把 `article-publish.md` 和最终公众号图转成 `wechat/publish-ready.md`。 / Convert `article-publish.md` and final WeChat images into `wechat/publish-ready.md`.
- `scripts/submit_wechat_draft.sh`：封装本地 WeChat publisher adapter 的 dry-run 和草稿创建；未配置适配器时只做本地 dry-run。 / Wrapper for local WeChat publisher adapter dry-run and draft creation. Without an adapter it only performs a local dry-run.
- `scripts/build_xiaohongshu_post.py`：从 `social-pack/content-pack.json` 生成小红书帖子初稿。 / Build a Xiaohongshu post draft from `social-pack/content-pack.json`.

脚本输出不能替代编辑判断。仍需人工/Agent 检查证据、评分、图片质量、字号比例、二维码真实性和发布状态。

Script output does not replace editorial judgment. The agent must still review evidence, scoring, image quality, typography scale, QR authenticity, and publication status.
