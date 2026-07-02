# Highlight Selection / 高光筛选

## 中文

### 目标

从逐字稿中提取最值得传播、最能支撑文章结构和图卡表达的高光片段。最终高光要能支撑：

- 开场钩子
- 文章章节结构
- 实操价值
- 故事或案例
- 清晰图片卡片
- 小红书和 X 二次分发

### 切分规则

1. 有时间戳时，先按 3-8 分钟的自然主题段切分。
2. 没有时间戳时，按话题变化、提问、案例、总结、强观点或明显金句切分。
3. 一个高光只表达一个可独立理解的观点，不要只截孤立一句话。
4. 候选片段优先 1-8 分钟，太长则继续拆分。

### 10 维评分

每项 0-5 分，总分 50 分。

| 维度 | 检查点 |
| --- | --- |
| 开场钩子 | 冲突、反差、问题、承诺，是否一句话让人停下 |
| 信息密度 | 单位时间内是否有足够新信息，不是松散铺垫 |
| 实用价值 | 方法、步骤、工具、清单、工作流、经验 |
| 故事性 | 起因、行动、结果、转折或具体案例 |
| 新奇性 | 反常识观点、意外数据、结论或经验 |
| 可引用性 | 能否变成标题、金句或图卡大字 |
| 独立完整度 | 脱离前后文后是否仍能看懂 |
| 视觉化潜力 | 能否变成流程、飞轮、对比、案例或知识卡 |
| 平台互动信号 | 最多在线观众、最高评论率、最高留存率、回放、分享、评论峰值 |
| 风险控制 | 避开隐私、敏感、夸大、误读 |

### 平台高光截图

当用户提供微信或视频平台高光截图时，输出 `platform-highlight-signals.md`。

- `最多在线观众`：说明话题吸引力或入场峰值，提升平台互动信号和钩子评分。
- `最高评论率`：说明讨论、提问、分歧或参与强，提升平台互动信号、故事性和实用价值。
- `最高留存率`：说明清晰度和价值密度较高，提升平台互动信号、信息密度和独立完整度。

平台截图不能替代逐字稿证据。没有逐字稿证据的内容只能标记为 `evidence_missing`。

### 选择规则

1. 生成 8-12 个候选。
2. 选择 5-8 个最终高光。
3. 尽量覆盖：钩子、方法、操作、案例、社群/活动桥接。
4. 两个候选表达同一点时，保留更短、更清楚、更可视化的。
5. 每个入选和落选候选都写一句理由。

## English

### Goal

Extract the most shareable and structurally useful moments from the transcript. Final highlights should support:

- opening hook
- article chapter structure
- practical value
- story or case
- clear image cards
- Xiaohongshu and X repurposing

### Segmentation Rules

1. With timestamps, split by natural 3-8 minute topic sections.
2. Without timestamps, split at topic changes, questions, cases, summaries, strong claims, or obvious quotes.
3. A highlight must express one standalone idea. Do not clip only one isolated sentence.
4. Prefer 1-8 minute candidates. Split very long candidates again.

### 10-Dimension Scorecard

Score each dimension 0-5. Total score is 50.

| Dimension | What To Check |
| --- | --- |
| Hook | Conflict, contrast, question, promise, one-line stop power |
| Information density | Enough new information per minute; not loose setup |
| Practical value | Methods, steps, tools, checklists, workflows, lessons |
| Story | Cause, action, result, turn, or concrete case |
| Novelty | Counterintuitive idea, surprising number, conclusion, or experience |
| Quoteability | Can become a title, quote, or large card text |
| Standalone completeness | Understandable without heavy surrounding context |
| Visual potential | Can become a flow, flywheel, comparison, case, or knowledge card |
| Platform interaction signal | Most online viewers, highest comment rate, highest retention rate, replay, shares, comment spike |
| Risk control | Avoids privacy, sensitive claims, exaggeration, or easy misreading |

### Platform Highlight Screenshots

When WeChat/video platform highlight screenshots are provided, create `platform-highlight-signals.md`.

- `最多在线观众`: audience entry peak or topic attraction. Raise platform signal and possibly hook score.
- `最高评论率`: discussion, questions, disagreement, or strong participation. Raise platform signal, story, and practical value.
- `最高留存率`: clarity and value density. Raise platform signal, information density, and standalone completeness.

Platform screenshots cannot replace transcript evidence. If transcript evidence is missing, mark `evidence_missing`.

### Selection Rules

1. Generate 8-12 candidates.
2. Select 5-8 final highlights.
3. Cover hook, method, operation, case, and community/event bridge when available.
4. If two candidates make the same point, keep the shorter, clearer, more visual one.
5. Write a short reason for every selected and rejected candidate.

## 输出格式 / Required Output

`highlight-candidates.md`:

```md
## h01

Timestamp: 0:11:32-0:17:21
Candidate title: Agent 团队效率提升 10 倍：一人一天做 MVP
Use: opening hook
Reason: strong number, contrast, and practical story
Evidence excerpt: ...
Quote candidates:
- ...
Image task: case
```

`highlight-scorecard.md`:

```md
| id | title | total | hook | density | practical | story | novelty | quote | standalone | visual | platform | risk | decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| h01 | ... | 46 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | selected |
```
