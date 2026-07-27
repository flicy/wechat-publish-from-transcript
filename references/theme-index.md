# 主题索引 / Theme Index

## 中文

排版阶段从这里选主题。一篇文章只用一个主题。

### 可用主题

| 主题 | 文件 | 主色 | 适合 |
|---|---|---|---|
| **Growth Orange 增长橙**（默认） | `references/theme-growth-orange.md` | `#E6532E` | 演讲 / 直播 / 访谈 / 会议 / 视频——本 Skill 的全部逐字稿场景。招牌是左侧橙色强调条的截图式标题块。 |

### 选择指南

- 未指定主题 → 默认 `growth-orange`。
- 内容偏科技 / 教程 / 数据密集 → 仍可用 `growth-orange`（数据卡片 + 步骤列表足够）；若安装了 gzh-design-skill，可借用它的科技类主题。
- 用户明确要别的风格 → 见「加主题」。

### 加主题

两条路：

1. **借用 gzh-design-skill 主题库**（推荐）：若环境装了 [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)，直接用它的 `references/theme-*.md`（墨绿 / 红白 / 禅意白 / 橄榄期刊 / 摸鱼绿 / 摸鱼票根等 6 套），并用它的 `references/theme-generator.md` 生成新主题。本 Skill 的 `scripts/validate_gzh_html.py` 与 `scripts/component_lint.py` 与它的校验规则同源，可直接把关。
2. **本仓库内新增**：复制 `theme-growth-orange.md` 结构，替换颜色 token，跑 `python3 scripts/component_lint.py` 到 0 ERROR，再在本文件登记一行。

主题文件必须包含：颜色 token 块、编号组件（内联样式 + `<span leaf="">`）、Markdown→组件映射、内容类型→组件搭配、组装骨架、使用频率。

## English

The typesetting stage picks a theme here. One article = one theme.

**Available:** **Growth Orange** (default, `references/theme-growth-orange.md`, accent `#E6532E`) — for talks / livestreams / interviews / meetings / video; signature is the screenshot-style title block with a left orange accent bar.

**Selection:** unspecified → default `growth-orange`. For other styles, either borrow themes from [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) (6 themes + a theme generator; this skill's validators are same-origin and can gate them), or add a theme in-repo by copying the `theme-growth-orange.md` structure, swapping color tokens, running `scripts/component_lint.py` to 0 ERROR, and registering a row here. A theme file must contain: a color-token block, numbered components (inline styles + `<span leaf="">`), a Markdown→component map, a content-type→component pairing, an assembly skeleton, and a usage-frequency table.
