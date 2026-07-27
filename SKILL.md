---
name: wechat-publish-from-transcript
description: Use when creating or publishing a 微信公众号 article from a talk, livestream, interview, meeting, video, transcript, or Notion page, especially when the task needs transcript-based highlights, evidence mapping, article drafting, Image 2.0/GPT Image prompt packs, reference-image style learning, QR-safe image planning, paste-ready WeChat HTML typesetting (theme system + dual-gate validation), WeChat draft/publish execution, or reusable Xiaohongshu/X content packs. 适合把转写稿做成微信文章、图片 Prompt、可直接粘贴的公众号排版 HTML、微信草稿载荷和跨平台社交内容包。
license: MIT
metadata:
  compatibility: Works with Agent Skills / SKILL.md compatible coding agents. Optional WeChat publisher adapter for draft submission.
---

# 微信发布全流程

把一个真实转写稿变成微信文章、图片提示词包、小红书帖子和 X 帖子的可复用资产。这是一个面向 Codex、Cursor、Cola、Claude 等编码代理的工作流包，不是"一次性写作提示"，而是把证据、写作、图片规划、微信草稿提交、小红书帖子和跨平台分发的完整流程。

每次运行都应当可以审计：能回到转写稿证据，能复用图片，能 dry-run，能追踪图片来源。

## 核心原则

1. 转写稿是唯一证据源。
2. 先做转写稿亮点提取再写作。
3. 所有主张、引用和例子必须有转写稿证据。
4. 用 `references/highlight-selection.md` 的 10 维评分卡评分。
5. 用平台截图信号增强排序和证据可信度。
6. 图片、封面、二维码必须来自真实文件，不用 AI 重绘。
7. 二维码、Logo、品牌资产不能用 AI 生成。
8. 微信草稿提交使用本地配置的 WeChat publisher adapter，不在 Skill 中绑定任何私密发布者。
9. 每场活动增加一张 `00-overview-recap` 总览图。
10. 输出 `image-prompts.md`，包含统一 Prompt 和每图/每平台/每证据的复用 Prompt。
11. 输出 `social-pack/content-pack.json`，供小红书和 X 复用。
12. 记录图片来源、合成方法、模型限制和最终文件路径，不声称没有验证过的模型。
13. 微信第一张图必须是 `2.35:1` 横图，例如 `assets/final/wechat/01-cover.png`。
14. 微信文章标题块和生成图片共享同一主色，使用截图式左强调条/浅底标题块。
15. 微信发布前生成 `wechat/publish-ready.md`，先 dry-run，再用本地适配器创建草稿/发布。
16. 图片和文章确认后，并行运行微信草稿 Agent 和小红书帖子 Agent；两个子 Agent 只读必要上下文，不重读转写稿。
17. 最后汇总输出路径、来源、图片出处、发布状态、限制，并询问是否需要修改。
18. 正文必须排版成可直接粘贴的公众号 HTML：扁平 `<section>` 嵌套 + 100% 内联样式 + 每段中文用 `<span leaf="">` 包裹，见 `references/typeset-wechat-html.md`。
19. 一篇文章只用一个主题（默认 `growth-orange`），从 `references/theme-index.md` 选，绝不混用。
20. 排版后必跑 `scripts/validate_gzh_html.py`，**0 ERROR** 才能交付；改主题组件后跑 `scripts/component_lint.py` 静态把关。
21. 排版不替代编辑判断：证据溯源、高光真实性、图注准确性、二维码真实性仍需人/Agent 复核。

## 流程

1. 解析输入：`references/input-contract.md`。
2. 创建 `plan.md`。
3. 从转写稿提取基础亮点候选。
4. 为候选亮点评分。
5. 合并平台截图信号增强排序。
6. 建立 `evidence-map.md`。
7. 起草 `article-source.md`，再生成 `article-publish.md`。
8. 规划图片方案，包含 `00-overview-recap`。
9. 生成 `image-prompts.md`，含证据、标题、总览图和参考图。
10. 生成图片：用真实二维码、品牌资产和参考图。
11. 记录图片来源。
12. 检查图片质量、平台信号、出处、限制和最终文件路径。
13. 排版正文：按 `references/typeset-wechat-html.md` 把 `article-publish.md` 排成主题化 HTML `wechat/article.html`，跑 `scripts/validate_gzh_html.py` 到 **0 ERROR**。
14. 按 `references/wechat-checklist.md` 做发布预检。
15. 生成 `social-pack/content-pack.json`。
16. 用 `references/wechat-draft-submit.md` 生成 `publish-ready.md` 并 dry-run。
17. 按 `references/parallel-publishing.md` 并行运行微信草稿 Agent 和小红书帖子 Agent。
18. 用本地 WeChat publisher adapter 创建微信草稿（优先传已排版 `wechat/article.html`）。
19. 输出路径、来源、限制和发布状态。

## 何时读取哪个文件

- 输入合同：`references/input-contract.md`。
- 亮点评分和选择：`references/highlight-selection.md`。
- 产品背景、参考图学习、小红书 X 扩展：`references/product-notes.md`。
- 安装到 Codex、Cursor、Cola、Claude 等 Agent 环境：`references/installation.md`。
- 图片、封面、总览图、参考图学习：`references/image-style.md`。
- 公众号正文排版（Markdown → 可粘贴 HTML）：`references/typeset-wechat-html.md`。
- 主题选择与新增主题：`references/theme-index.md`。
- 默认主题组件库（增长橙）：`references/theme-growth-orange.md`。
- 发布预检：`references/wechat-checklist.md`。
- 微信草稿提交：`references/wechat-draft-submit.md`。
- 微信发布适配器契约：`references/wechat-publisher-adapter.md`。
- 微信草稿和小红书帖子并行流程：`references/parallel-publishing.md`。
- 跨平台社交内容包：`references/social-pack-schema.md`。
- 完整 SOP：`references/sop.md`。

## 脚本

- `scripts/extract_highlights.py`：生成初始亮点候选框架。
- `scripts/build_content_pack.py`：把标题和亮点生成 `content-pack.json` 框架。
- `scripts/compose_qrcode_card.py`：把真实二维码合成到卡片。
- `scripts/validate_assets.py`：检查图片尺寸和比例。
- `scripts/build_wechat_publish_ready.py`：从 `article-publish.md` 和真实图片生成 `wechat/publish-ready.md`（按 `<!-- 图片 NN -->` 序号动态匹配图片，缺图直接报错，主题无关）。
- `scripts/submit_wechat_draft.sh`：调用本地 WeChat publisher adapter 的 dry-run 或真实提交。
- `scripts/build_xiaohongshu_post.py`：从 `social-pack/content-pack.json` 生成小红书帖子。
- `scripts/validate_gzh_html.py`：公众号 HTML 合规校验（动态关卡）。排版后必跑，0 ERROR 才交付。
- `scripts/component_lint.py`：组件库源头检查（静态关卡）。改主题组件后跑。
- `scripts/wrap_preview.py`：把合规片段包成带「复制到公众号」按钮的浏览器预览页。

多数脚本是可选辅助工具，但 `validate_gzh_html.py` 是硬性关卡（排版后必跑）。最终标题/Agent 决策、证据、图片质量、二维码合成、排版合规和发布状态仍由代理和用户确认。
