# Full SOP / 完整 SOP

## 中文

这份 SOP 是 `SKILL.md` 的详细执行版。`SKILL.md` 保持短而可发现，本文件保留完整发布链路。本 Skill 是平台无关工作流包，可从 Codex、Cursor、Cola、Claude 或通用 `AGENTS.md` 入口加载；安装方式见 `references/installation.md`。

### 流程

1. 解析输入。
2. 创建 `plan.md`。
3. 从逐字稿提取候选高光。
4. 用 10 维评分表筛选高光。
5. 合并可选的微信/视频平台高光信号。
6. 建立 `evidence-map.md`。
7. 起草 `article-source.md`。
8. 整理 `article-publish.md`。
9. 按最终高光规划图片，包括 `00-overview-recap`。
10. 生成 `image-prompts.md`，结合逐字稿、文章、配图计划和参考图。
11. 生成或合成图片。
12. 记录图片来源：模型/来源、本地合成、最终路径、模型限制。
13. 跑微信发布前检查，确认封面为 `2.35:1`，文章标题主色和图片主色一致。
14. 生成 `social-pack/content-pack.json`。
15. 生成 `wechat/publish-ready.md`，所有图片引用必须是本地真实文件。
16. 按 `references/parallel-publishing.md` 启动两个同步任务：微信草稿 Agent 和小红书帖子 Agent。
17. 微信草稿 Agent 运行 dry-run、内容确认，并在用户确认后用本地 WeChat publisher adapter 创建草稿或发布，记录 `media_id` 或草稿标识。
18. 小红书帖子 Agent 读取 `content-pack.json` 生成 `xiaohongshu/post.md` 和 `xiaohongshu/card-sequence.md`。
19. 回报输出路径、发布状态、小红书帖子状态和仍需人工确认的事项。
20. 交付时明确说明输入、输出、图片来源、限制，并询问是否需要修改。

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

- 逐字稿优先。
- 证据先于写作。
- 高光先于章节。
- 一个高光对应一张解释图。
- 章节图前必须有一张全场总回顾图。
- Prompt 是交付物，必须可复用。
- 图片来源是交付物的一部分，不能无依据声称使用了某个模型。
- 中文文字和字号比例要求高时，优先“模型生成无字视觉 + 本地排版”。
- 二维码只用真实文件。
- 默认先草稿，除非用户明确要求正式发布。
- 微信草稿不是简单导出文件，必须构建 `publish-ready.md`、dry-run、提交草稿并记录 `media_id`。
- 微信同步到平台时使用节省 token 的方式：子任务只读 `publish-ready.md`、图片清单和检查表，不重新读取逐字稿。
- 小红书帖子生成与微信草稿任务并行，子任务只读 `content-pack.json` 和图卡计划。
- 内容确认是 API 提交前的必需门：标题、摘要、封面、图片、姓名、二维码、密钥、评论设置都要检查。
- 每次都输出结构化资产，方便后续小红书和 X 工作流复用。
- 多平台只做加载入口适配，核心执行规则以本 Skill 包为准。

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
13. Run the WeChat preflight checklist; confirm the cover is `2.35:1` and article title accent color matches the image accent color.
14. Build `social-pack/content-pack.json`.
15. Build `wechat/publish-ready.md` with real local image references.
16. Start two parallel tasks via `references/parallel-publishing.md`: WeChat Draft Agent and Xiaohongshu Post Agent.
17. The WeChat Draft Agent runs dry-run, content confirmation, and after user confirmation uses the local WeChat publisher adapter for draft/publish, recording `media_id` or the draft identifier.
18. The Xiaohongshu Post Agent reads `content-pack.json` and builds `xiaohongshu/post.md` plus `xiaohongshu/card-sequence.md`.
19. Report output paths, publication status, Xiaohongshu post status, and remaining manual checks.
20. At handoff, summarize inputs, outputs, image provenance, limitations, and ask whether changes are needed.

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
- Use a token-saving platform sync path for WeChat: the subtask reads only `publish-ready.md`, image manifests, and the checklist, not the full transcript.
- Run Xiaohongshu post generation in parallel with the WeChat draft task. The subtask reads only `content-pack.json` and card plans.
- Content confirmation is a required gate before API draft creation: title, summary, cover, images, names, QR codes, secrets, and comment settings must be checked.
- Output structured assets for future Xiaohongshu and X workflows.
- Multi-platform usage should adapt only the loading entry point; the execution rules remain in this Skill package.
