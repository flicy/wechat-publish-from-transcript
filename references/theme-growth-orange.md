# 公众号排版组件 —— Growth Orange（增长橙）

> **这是本 Skill 的默认主题**，专为「逐字稿改写的公众号文章」设计：演讲 / 直播 / 访谈 / 会议 / 视频。
>
> **必须遵守的平台限制**（公众号编辑器会剥离以下一切，违反即丢样式）：
> - 不用 `<style>`/`<script>`/`<div>`、CSS `class`/`id`、外链 CSS、CSS 变量 `var(--x)`
> - 不用 `position:fixed/absolute/sticky`、`float`、`@media`/`@keyframes`/`@import`、`display:grid`
> - 只用内联 `style`、`<section>/<p>/<span>/<strong>/<em>/<img>`、`display:flex`、`linear-gradient`、`border-radius`、`box-shadow`
> - **每一段中文都必须用 `<span leaf="">…</span>` 包裹**——这是公众号粘贴解析器保留样式的关键，漏包即大面积丢样式
> - 空行占位用 `<span leaf=""><br></span>`，不要用 `&nbsp;` 堆叠
>
> 生成后必须跑 `scripts/validate_gzh_html.py`，**0 ERROR** 才能交付。组件库本身由 `scripts/component_lint.py` 静态把关。

---

## 颜色跟随主题

```
主题色：     #E6532E（增长橙）
主题色深：   #B23A1D（深橙，标题/强调）
主题色中：   #F0906F（浅橙，渐变/描边）
主题色浅：   #FBE0D6（浅色块底）
主题色浅浅： #FFF5EF（极浅底，标题块/卡片底）
橙色分割线： #F3C9B8（分割线）
标题色：     #1F2937（近黑）
文字色：     #374151（深灰正文）
辅助文字色： #9CA3AF（中灰，注释/英文 tag）
分割线色：   #E5E7EB（浅灰辅助分割线）
正文字号：   15px
行高：       1.8
字间距：     0.5px
内容宽度：   677px
段落间距：   段间约 18px
```

字体：`-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

> **颜色跟随规则**：下面所有组件用的 `#E6532E / #B23A1D / #F0906F / #FBE0D6 / #FFF5EF / #F3C9B8` 都是本主题 token。换主题时整体替换为对应主题 token，不要混用其它主题的色值。

---

## 组件 1 外层容器

> 一篇文章一个容器，所有内容都放进这一个 `<section>`。

```html
<section style="max-width:677px;margin:0 auto;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.8;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 其它组件依次堆在这里 -->

</section>
```

---

## 组件 2 封面标题块（截图式：左侧强调色条 + 浅色底）

> 这是本 Skill 的招牌标题样式，与封面图强调色一致（`#E6532E`）。文章第一屏用它。

```html
<section style="margin:8px 10px 30px;background:#FFF5EF;border-left:6px solid #E6532E;border-radius:10px;padding:24px 22px;">
  <p style="font-size:11px;color:#E6532E;font-weight:700;letter-spacing:3px;margin:0 0 10px;text-transform:uppercase;">
    <span leaf="">{{ENGLISH KICKER}}</span>
  </p>
  <h1 style="font-size:24px;font-weight:900;color:#1F2937;margin:0 0 12px;line-height:1.4;letter-spacing:0.5px;">
    <span leaf="">{文章主标题}</span>
  </h1>
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.7;">
    <span leaf="">{一句话导语，来自逐字稿最有张力的判断}</span>
  </p>
  <p style="font-size:12px;color:#9CA3AF;margin:14px 0 0;letter-spacing:1px;">
    <span leaf="">{讲者 / 来源} · {日期}</span>
  </p>
</section>
```

---

## 组件 3 全场回顾图（00-overview-recap）

> 放在封面标题块之后、正文章节之前。一张图回顾全场，是本 Skill 的硬性要求。

```html
<section style="padding:0 10px 28px;">
  <img src="{00-overview-recap 相对路径}" style="width:100%;border-radius:12px;display:block;box-shadow:0 6px 24px -8px rgba(230,83,46,0.25);" />
  <p style="text-align:center;font-size:12px;color:#9CA3AF;margin:10px 0 0;letter-spacing:1px;">
    <span leaf="">▲ 一张图回顾全场</span>
  </p>
</section>
```

---

## 组件 4 三栏要点卡（TL;DR / 本期要点）

> 开篇用 3 个要点卡概括全场，读者 10 秒抓住主线。要点必须是真实高光，不是凑数。

```html
<section style="padding:0 10px 30px;">
  <p style="font-size:13px;color:#9CA3AF;margin:0 0 14px;letter-spacing:2px;">
    <span leaf="">📌 本期要点</span>
  </p>
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#FFF5EF;border:1px solid #FBE0D6;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;">
      <p style="display:inline-block;background:#E6532E;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:700;color:#1F2937;margin:0;line-height:1.6;"><span leaf="">{要点一}</span></p>
    </section>
    <section style="flex:1;background:#FFF5EF;border:1px solid #FBE0D6;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;">
      <p style="display:inline-block;background:#E6532E;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:700;color:#1F2937;margin:0;line-height:1.6;"><span leaf="">{要点二}</span></p>
    </section>
    <section style="flex:1;background:#FFF5EF;border:1px solid #FBE0D6;border-radius:10px;padding:16px 12px;text-align:center;">
      <p style="display:inline-block;background:#E6532E;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:700;color:#1F2937;margin:0;line-height:1.6;"><span leaf="">{要点三}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 5 橙色渐变分割线

> 章节之间、大段落之间用。`<span leaf=""><br></span>` 撑高，避免空 section 被吞。

```html
<section style="padding:6px 10px;">
  <section style="height:1px;background:linear-gradient(to right,transparent,#F0906F,#E6532E,#F0906F,transparent);margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 6 章节标题（序号 + 英文 tag + 中文标题）

> 每个最终高光一个章节。第一个章节用 `margin-top:40px`，后续 `margin-top:48px`。

```html
<section style="margin-top:48px;margin-bottom:24px;padding:0 10px;">
  <section style="display:flex;align-items:center;margin-bottom:18px;padding-bottom:14px;border-bottom:3px solid #E6532E;">
    <span style="display:inline-block;background:#E6532E;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">01</span></span>
    <section>
      <p style="font-size:10px;color:#E6532E;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
        <span leaf="">{{ENGLISH TAG}}</span>
      </p>
      <h3 style="font-size:18px;font-weight:800;color:#1F2937;margin:0;letter-spacing:0.5px;">
        <span leaf="">{章节标题}</span>
      </h3>
    </section>
  </section>
</section>
```

---

## 组件 7 正文段落 + 行内高亮

> 正文主力。关键句用 `border-bottom` 橙色描边强调，一篇里克制使用（每节 1–2 处）。

```html
<section style="padding:0 10px;">
  <p style="font-size:15px;color:#374151;margin:0 0 18px;line-height:1.8;">
    <span leaf="">{正文段落。把逐字稿的口语顺成书面语，但保留讲者的判断与语气。}</span>
    <span style="border-bottom:2px solid #E6532E;color:#B23A1D;font-weight:700;"><span leaf="">{需要强调的关键句}</span></span>
    <span leaf="">{段落剩余部分。}</span>
  </p>
</section>
```

---

## 组件 8 小标题

> 章节内部的二级小标题，不用序号。

```html
<section style="padding:0 10px;">
  <h4 style="font-size:16px;font-weight:800;color:#B23A1D;margin:26px 0 12px;padding-left:10px;border-left:4px solid #F0906F;line-height:1.5;">
    <span leaf="">{小标题}</span>
  </h4>
</section>
```

---

## 组件 9 讲者原话引用块

> 逐字稿文章的核心组件：还原讲者原话，保留「谁说的」。引用必须能在 evidence-map 里找到出处。

```html
<section style="padding:0 10px;">
  <section style="background:#FFF5EF;border-left:4px solid #E6532E;border-radius:0 10px 10px 0;padding:18px 20px;margin:0 0 20px;">
    <p style="font-size:34px;color:#F0906F;font-weight:900;margin:0;line-height:0.5;">
      <span leaf="">"</span>
    </p>
    <p style="font-size:15px;color:#1F2937;font-weight:600;margin:10px 0 12px;line-height:1.8;">
      <span leaf="">{讲者原话，可轻度顺句但不动观点}</span>
    </p>
    <p style="text-align:right;font-size:12px;color:#9CA3AF;margin:0;letter-spacing:1px;">
      <span leaf="">—— {讲者姓名 / 身份}</span>
    </p>
  </section>
</section>
```

---

## 组件 10 关键洞察提示框

> 提炼出的方法论 / 金句 / 可执行建议，用提示框凸显。比正文高一级视觉权重。

```html
<section style="padding:0 10px;">
  <section style="background:#FBE0D6;border-radius:12px;padding:18px 20px;margin:0 0 20px;">
    <p style="font-size:12px;color:#B23A1D;font-weight:800;letter-spacing:2px;margin:0 0 8px;">
      <span leaf="">💡 关键洞察</span>
    </p>
    <p style="font-size:15px;color:#1F2937;margin:0;line-height:1.8;">
      <span leaf="">{一句话洞察或可执行建议}</span>
    </p>
  </section>
</section>
```

---

## 组件 11 编号步骤列表

> 讲者给出的步骤 / 流程 / 清单。

```html
<section style="padding:0 10px;">
  <section style="display:flex;margin-bottom:12px;">
    <span style="display:inline-block;flex:none;background:#E6532E;color:#FFFFFF;font-size:13px;font-weight:800;width:24px;height:24px;line-height:24px;text-align:center;border-radius:50%;margin-right:12px;"><span leaf="">1</span></span>
    <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;">
      <strong style="color:#1F2937;"><span leaf="">{步骤标题}：</span></strong>
      <span leaf="">{步骤说明}</span>
    </p>
  </section>
  <!-- 2 / 3 同结构，序号递增 -->
</section>
```

---

## 组件 12 数据卡片

> 讲者提到的关键数字（增长 / 转化 / 规模）。数字要大，标签要小。

```html
<section style="padding:0 10px 8px;">
  <section style="display:flex;justify-content:space-between;background:#FFF5EF;border:1px solid #FBE0D6;border-radius:12px;padding:20px 16px;margin-bottom:20px;">
    <section style="flex:1;text-align:center;">
      <p style="font-size:28px;font-weight:900;color:#E6532E;margin:0;line-height:1.2;"><span leaf="">{数字}</span></p>
      <p style="font-size:12px;color:#9CA3AF;margin:6px 0 0;letter-spacing:1px;"><span leaf="">{指标名}</span></p>
    </section>
    <section style="flex:1;text-align:center;border-left:1px solid #F3C9B8;">
      <p style="font-size:28px;font-weight:900;color:#E6532E;margin:0;line-height:1.2;"><span leaf="">{数字}</span></p>
      <p style="font-size:12px;color:#9CA3AF;margin:6px 0 0;letter-spacing:1px;"><span leaf="">{指标名}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 13 章节说明图

> 一个高光一张说明图。图注简短，指向本节点点。

```html
<section style="padding:0 10px 24px;">
  <img src="{NN-slug 相对路径}" style="width:100%;border-radius:12px;display:block;box-shadow:0 4px 20px -8px rgba(31,41,55,0.2);" />
  <p style="text-align:center;font-size:12px;color:#9CA3AF;margin:10px 0 0;letter-spacing:1px;">
    <span leaf="">▲ {图注}</span>
  </p>
</section>
```

---

## 组件 14 END 分割线 + 作者签名

> 文章结尾。社群二维码图放这里（真实二维码，绝不 AI 重绘）。

```html
<section style="margin-top:48px;padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right,transparent,#F0906F,#E6532E,#F0906F,transparent);margin:0 0 24px;">
    <span leaf=""><br></span>
  </section>
  <p style="text-align:center;font-size:13px;color:#9CA3AF;margin:0 0 6px;letter-spacing:2px;">
    <span leaf="">· END ·</span>
  </p>
  <p style="text-align:center;font-size:13px;color:#374151;margin:0;line-height:1.7;">
    <span leaf="">{作者 / 栏目署名}</span>
  </p>
</section>
```

---

## Markdown → 组件映射

| Markdown 元素 | 用哪个组件 |
|---|---|
| `# 一级标题` | 组件 2 封面标题块（不直接输出 `<h1>` 裸标题） |
| `## 二级标题`（章节） | 组件 6 章节标题 |
| `### 三级标题` | 组件 8 小标题 |
| 正文段落 | 组件 7 正文段落 |
| `> 引用` | 组件 9 讲者原话引用块 |
| `1. / - 列表` | 组件 11 编号步骤列表 |
| `![图](path)` | 组件 13 章节说明图（00 图用组件 3） |
| 关键数字 | 组件 12 数据卡片 |
| 方法论 / 建议 | 组件 10 关键洞察提示框 |
| `---` | 组件 5 渐变分割线 |

## 内容类型 → 组件搭配

| 内容类型 | 推荐搭配 |
|---|---|
| 演讲 / 分享 | 封面 + 回顾图 + 三栏要点 + 章节（多）+ 引用块（多）+ 洞察框 + END |
| 访谈 / 对谈 | 封面 + 三栏要点 + 章节 + **大量引用块**（区分不同讲者）+ END |
| 直播复盘 | 封面 + 回顾图 + 数据卡片 + 章节 + 步骤列表 + END |
| 会议 / 纪要 | 封面 + 三栏要点 + 章节 + 步骤列表 + 洞察框 + END |

## 组装骨架

```
组件1 外层容器
├─ 组件2 封面标题块
├─ 组件3 全场回顾图
├─ 组件4 三栏要点卡
├─ 组件5 分割线
├─ 组件6 章节标题 01
│   ├─ 组件7 正文段落
│   ├─ 组件9 引用块
│   └─ 组件13 说明图
├─ 组件6 章节标题 02 …（循环）
├─ 组件14 END + 签名
```

## 使用频率

| 组件 | 频率 |
|---|---|
| 1 外层容器 / 2 封面 / 6 章节 / 7 正文 / 14 END | 高（每篇必用） |
| 3 回顾图 / 4 要点卡 / 9 引用块 / 13 说明图 | 高 |
| 5 分割线 / 8 小标题 / 10 洞察框 | 中 |
| 11 步骤列表 / 12 数据卡片 | 中低（按需） |
