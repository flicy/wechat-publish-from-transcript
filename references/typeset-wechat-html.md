# 公众号正文排版 / Typeset WeChat Article HTML

## 中文

本 Skill 的管线产出 `article-publish.md`（Markdown）和配图，但**公众号编辑器不接受 Markdown**——它只吃富文本 HTML，而且会剥离几乎所有样式手段。这份文档定义「Markdown → 可直接粘贴的公众号 HTML」这一层，方法论改编自 [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)（MIT）。

### 为什么必须这样做（平台硬约束）

公众号编辑器粘贴时会剥离：`<style>`、`<script>`、`<div>`、`class`、`id`、外链 CSS、CSS 变量 `var(--x)`、`display:grid`、`position:fixed/absolute/sticky`、`float`、`@media`/`@keyframes`/`@import`、web 字体文件。

因此输出必须满足：

1. **扁平 `<section>` 嵌套**，样式 100% 内联（`style="…"`）。
2. **每一段中文都用 `<span leaf="">…</span>` 包裹**——`leaf` 属性是公众号粘贴解析器保留样式的钥匙，漏包即大面积丢样式。
3. 空行占位用 `<span leaf=""><br></span>`。
4. 只输出 `<section>…</section>` **片段**，不要 `<!DOCTYPE>/<html>/<head>/<body>`。

### 在管线中的位置

```
article-publish.md（Markdown + <!-- 图片 NN --> 占位）
        │  配图已生成（assets/final/wechat/*.png）
        ▼
【排版阶段 · 本文档】 typeset → wechat/article.html（合规片段）
        ▼
wechat/publish-ready.md（frontmatter + 元信息）
        ▼
微信草稿 Agent：validate_gzh_html.py 0 ERROR → dry-run → 用户确认 → adapter 提交
```

排版阶段在「配图就绪之后、草稿提交之前」。它消费 `article-publish.md` 与最终配图，产出 `wechat/article.html`。

### 排版工作流（6 步）

1. **归一化输入**：`article-publish.md` 已是干净 Markdown 则直接进入下一步；若来源是 docx/pdf/txt，先归一化成 Markdown 再排版，**不要边转边排**。
2. **选主题**：读 `references/theme-index.md`，按内容类型选（演讲/访谈/直播/会议）。未指定时默认 `growth-orange`。一篇文章只用一个主题，绝不混用。
3. **读组件（只读一次）**：读选定的 `references/theme-{name}.md` 和（如需）通用组件。生成 HTML 前不要反复重读参考文件。
4. **映射生成**：按主题文件里的「Markdown → 组件映射」把文章逐段转成组件 HTML。主题组件优先；缺组件才用通用库；都没有再造。中文一律 `<span leaf="">` 包裹。
5. **本地校验（硬性）**：跑 `python3 scripts/validate_gzh_html.py wechat/article.html`，**必须 0 ERROR** 才算通过（WARNING 可选修）。有 ERROR 回到第 4 步修，不要带病交付。
6. **输出**：片段存为 `wechat/article.html`；交付文件命名 `{标题}_公众号排版_{theme}.html`。可选 `python3 scripts/wrap_preview.py wechat/article.html` 生成带「复制到公众号」按钮的浏览器预览页，用户点开即可一键复制粘贴。

### 硬性规则

- 一篇文章一个主题，不混用。
- 中文必须 `<span leaf="">` 包裹；校验器报「没有 span leaf」即 ERROR，必须修。
- 二维码 / Logo / 品牌资产只用用户提供的真实文件，**绝不 AI 重绘**；二维码图按主题的图片组件嵌入。
- 封面标题块强调色（`#E6532E`）必须与封面图强调色一致。
- 输出只是 `<section>` 片段；预览外壳（含 `<script>/<style>` 的复制按钮页）由 `wrap_preview.py` 单独生成，**不参与校验**。
- 排版不替代编辑判断：证据是否溯源、高光是否真实、图注是否准确，仍需人/Agent 复核。

### 与发布适配器 / 草稿的关系

`wechat/article.html` 是正文的最终形态。`references/wechat-publisher-adapter.md` 的适配器**优先接收已排版 HTML**（`--html wechat/article.html`）；没有适配器时，用户可直接把 `article.html`（或预览页）粘贴进公众号编辑器。`publish-ready.md` 仍保留 frontmatter（title/author/summary/coverImage）与 Markdown 正文，作为元信息与回退路径。

## English

The pipeline produces `article-publish.md` (Markdown) plus images, but the WeChat MP editor does not accept Markdown — it takes rich-text HTML and strips almost every styling mechanism. This document defines the "Markdown → paste-ready WeChat HTML" layer, adapted from [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) (MIT).

**Platform constraint:** WeChat strips `<style>`, `<script>`, `<div>`, `class`, `id`, external CSS, CSS variables, grid, positioning, float, media queries, animations, and web fonts. So the output must be flat `<section>` nesting with 100% inline styles, every Chinese run wrapped in `<span leaf="">…</span>` (the `leaf` attribute is what WeChat's paste parser preserves), and delivered as a bare `<section>` fragment (no `<!DOCTYPE>/<html>/<head>/<body>`).

**Position in pipeline:** after images are ready and before draft submission. It consumes `article-publish.md` + final images and produces `wechat/article.html`.

**Workflow (6 steps):** (1) normalize input to clean Markdown first; (2) pick one theme from `theme-index.md` (default `growth-orange`), never mix; (3) read the chosen `theme-{name}.md` once; (4) map Markdown → theme components, wrapping all Chinese in `<span leaf="">`; (5) run `scripts/validate_gzh_html.py` and reach **0 ERROR** before passing; (6) output the fragment to `wechat/article.html`, optionally wrapped by `scripts/wrap_preview.py` into a copy-to-WeChat preview page.

**Hard rules:** one theme per article; Chinese must be `<span leaf="">`-wrapped; QR/logo/brand assets are real files only, never AI-redrawn; the cover title-block accent (`#E6532E`) must match the cover image accent; output is a fragment only (the preview shell with copy button is generated separately and is not validated). The publisher adapter prefers the typeset HTML (`--html wechat/article.html`); without an adapter, users paste `article.html` (or the preview page) straight into the editor.
