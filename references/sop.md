# Full SOP / 完整 SOP

## 中文

这份 SOP 是 `SKILL.md` 的详细执行伴侣。`SKILL.md` 保持简洁和可发现；完整发布流程放这里。本 Skill 是平台中立的 workflow 包，可从 Codex、Cursor、Cola、Claude 或通用 `AGENTS.md` 入口加载。见 `references/installation.md`。

### 流程

1. 解析输入。
2. 创建 `plan.md`。
3. 从转写稿提取基础亮点候选。
4. 用 10 维评分卡评分。
5. 合并可选微信/视频平台亮点信号。
6. 建立 `evidence-map.md`。
7. 起草 `article-source.md`。
8. 生成 `article-publish.md`。
9. 从最终亮点规划图片，包含 `00-overview-recap`。
10. 生成 `image-prompts.md`，含转写稿、文章、图片计划和参考图。
11. 生成或合成图片。
12. 记录图片出处：模型/来源、本地合成、最终文件路径和模型限制。
13. 排版正文：按 `references/typeset-wechat-html.md` 把 `article-publish.md` 排成主题化 HTML `wechat/article.html`（默认 `growth-orange` 主题），跑 `scripts/validate_gzh_html.py` 到 **0 ERROR**。
14. 运行微信预检清单；确认封面 `2.35:1`，文章标题强调色和图片强调色一致。
15. 生成 `social-pack/content-pack.json`。
16. 生成 `wechat/publish-ready.md`，用真实本地图片引用。
17. 按 `references/parallel-publishing.md` 启动两个并行任务：微信草稿 Agent 和小红书帖子 Agent。
18. 微信草稿 Agent 运行 dry-run、内容确认，用户确认后用本地 WeChat publisher adapter 创建草稿/发布（优先传已排版 `wechat/article.html`），记录 `media_id` 或草稿标识。
19. 小红书帖子 Agent 读取 `content-pack.json`，生成 `xiaohongshu/post.md` 和 `xiaohongshu/card-sequence.md`。
20. 报告输出路径、发布状态、小红书帖子状态和剩余手动检查。
21. 交接时汇总输入、输出、图片出处、限制，并询问是否需要修改。

### 必需文件

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
│   ├── article.html
│   ├── preview-checklist.md
│   ├── publish-ready.md
│   └── draft-submit-report.md
├── xiaohongshu/
│   ├── post.md
│   └── card-sequence.md
└── social-pack/
    └── content-pack.json
```

### 原则

- 转写稿优先。
- 证据先于写作。
- 亮点先于章节。
- 一个亮点一张说明图。
- 一张全场回顾图先于章节图。
- Prompt 是交付物，必须可复用。
- 图片出处是交付物的一部分。除非运行使用了明确、可验证的模型路径，否则不声称模型。
- 当中文文字或排版比例重要时，优先模型辅助无文字视觉加本地排版合成。
- 只用真实二维码。
- 发布前先草稿，除非用户明确要求发布。
- 微信草稿不只是文件导出。生成 `publish-ready.md`、dry-run、本地 WeChat publisher adapter 提交草稿，并记录 `media_id` 或草稿标识。
- 正文排版成可粘贴 HTML 是交付物的一部分：扁平 `<section>` + 内联样式 + 中文 `<span leaf="">` 包裹，`validate_gzh_html.py` 0 ERROR 才算完成；一篇文章一个主题。
- 使用 token 节省的平台同步路径：子任务只读 `publish-ready.md`、图片清单和清单，不读整篇转写稿。
- 小红书帖子生成与微信草稿任务并行。子任务只读 `content-pack.json` 和卡片计划。
- 内容确认是 API 草稿创建前的必需门：标题、摘要、封面、图片、名字、二维码、秘密和评论设置必须检查。
- 输出结构化资产，供未来小红书和 X 工作流复用。
- 多平台使用只适配加载入口；执行规则保留在本 Skill 包。

## English

This SOP is the detailed execution companion to `SKILL.md`. Keep `SKILL.md` concise and discoverable; keep the complete publishing process here. This Skill is a platform-neutral workflow package that can be loaded from Codex, Cursor, Cola, Claude, or a generic `AGENTS.md` entry. See `references/installation.md`.

### Flow

1. Resolve inputs.
2. Create `plan.md`.
3. Extract transcript-based highlight candidates.
4. Score highlights with the 10-dimension scorecard.
5. Merge optional WeChat/video platform highlight signals.
6. Build `evidence-map.md`.
7. Draft `article-source.md`.
8. Prepare `article-publish.md`.
9. Plan images from final highlights, including `00-overview-recap`.
10. Generate `image-prompts.md` from transcript, article, image plan, and reference images.
11. Generate or compose images.
12. Record image provenance: model/source, local composition, final file paths, and model limitations.
13. Typeset the body: per `references/typeset-wechat-html.md`, render `article-publish.md` into themed HTML `wechat/article.html` (default `growth-orange` theme); run `scripts/validate_gzh_html.py` to **0 ERROR**.
14. Run the WeChat preflight checklist; confirm the cover is `2.35:1` and article title accent color matches the image accent color.
15. Build `social-pack/content-pack.json`.
16. Build `wechat/publish-ready.md` with real local image references.
17. Start two parallel tasks via `references/parallel-publishing.md`: WeChat Draft Agent and Xiaohongshu Post Agent.
18. The WeChat Draft Agent runs dry-run, content confirmation, and after user confirmation uses the local WeChat publisher adapter for draft/publish (preferring the typeset `wechat/article.html`), recording `media_id` or the draft identifier.
19. The Xiaohongshu Post Agent reads `content-pack.json` and builds `xiaohongshu/post.md` plus `xiaohongshu/card-sequence.md`.
20. Report output paths, publication status, Xiaohongshu post status, and remaining manual checks.
21. At handoff, summarize inputs, outputs, image provenance, limitations, and ask whether changes are needed.

### Required Files

The required output tree is the same as the Chinese section above.

### Principles

- Transcript first.
- Evidence before writing.
- Highlights before chapters.
- One highlight, one explanation image.
- One whole-session recap image before chapter images.
- Prompts are deliverables and must be reusable.
- Image provenance is part of the deliverable. Never claim a model unless the run used an explicit, verifiable model path.
- When Chinese text or typography ratios matter, prefer model-assisted text-free visuals plus local typography composition.
- Real QR codes only.
- Draft before publish unless the user explicitly asks to publish.
- A WeChat draft is not just a file export. Build `publish-ready.md`, dry-run with the local WeChat publisher adapter, submit draft, and record the `media_id` or draft identifier.
- A paste-ready typeset HTML body is part of the deliverable: flat `<section>` + inline styles + Chinese wrapped in `<span leaf="">`, complete only when `validate_gzh_html.py` passes at 0 ERROR; one theme per article.
- Use a token-saving platform sync path for WeChat: the subtask reads only `publish-ready.md`, image manifests, and the checklist, not the full transcript.
- Run Xiaohongshu post generation in parallel with the WeChat draft task. The subtask reads only `content-pack.json` and card plans.
- Content confirmation is a required gate before API draft creation: title, summary, cover, images, names, QR codes, secrets, and comment settings must be checked.
- Output structured assets for future Xiaohongshu and X workflows.
- Multi-platform usage should adapt only the loading entry point; the execution rules remain in this Skill package.
