# WeChat Preflight Checklist / 微信发布前检查

Before creating a WeChat draft or publishing, create `wechat/preview-checklist.md`.

创建微信草稿或正式发布前，必须生成 `wechat/preview-checklist.md`。

```md
# WeChat Preview Checklist / 微信预览检查表

- [ ] Title has no typo / 标题无错别字
- [ ] Summary is concise and platform-safe / 摘要简洁且平台安全
- [ ] Cover exists and displays correctly / 封面存在且显示正常
- [ ] First WeChat image is `assets/final/wechat/01-cover.png` and uses `2.35:1` ratio / 公众号第一张图为 `2.35:1` 封面图
- [ ] Key title/subject stays in the central safe area / 标题和主体位于中心安全区
- [ ] Article title block accent color matches the generated image accent color / 文章标题块主色和生成图片主色一致
- [ ] Title block uses screenshot style: left accent bar, pale background, dark text / 标题块采用左侧主色条、浅色底、深色文字的截图式样
- [ ] Inline images exist and display correctly / 正文图片存在且显示正常
- [ ] WeChat inline chapter images are landscape 16:9 or near 16:9 / 公众号章节图为横版 16:9 或近似 16:9
- [ ] Xiaohongshu 3:4 vertical cards are not mixed into WeChat body / 没有把小红书 3:4 竖图混入公众号正文
- [ ] Image text has no obvious typo / 图片文字无明显错误
- [ ] Image title/subtitle scale follows `references/image-style.md` / 图片标题和副标题比例符合设计规范
- [ ] Main illustration/diagram is visually heavier than the headline on explanation images / 解释图的主体图解比标题更重
- [ ] `00-overview-recap` explains the whole session with evidence-backed people, topics, questions, tools, and conclusions / 总回顾图能用证据支撑人物、议题、问题、工具和结论
- [ ] `image-prompts.md` exists and includes unified master prompt plus WeChat/Xiaohongshu per-image prompts / 已输出统一母 Prompt 和逐图 Prompt
- [ ] Chapter explanation images match final highlights / 章节解释图对应最终高光
- [ ] Each image explains one idea / 每张图只解释一个观点
- [ ] Xiaohongshu cards are 3:4 vertical, clear, light, and easy to understand / 小红书图卡为 3:4，清晰、不累、易懂
- [ ] Official Account QR code uses the real provided file if used / 如使用公众号二维码，必须是真实文件
- [ ] Community QR code uses the real provided file if used / 如使用社群二维码，必须是真实文件
- [ ] Speaker names are correct / 嘉宾姓名正确
- [ ] Event issue, date, and activity name are correct / 期数、日期、活动名正确
- [ ] Claims and quotes are supported by transcript evidence / 观点和引用有逐字稿证据
- [ ] No AppSecret or private credentials appear in output files / 输出文件不包含 AppSecret 或私密凭证
- [ ] Source URL / 阅读原文 is correct if used / 如使用阅读原文，链接正确
- [ ] Comment settings match user preference / 评论设置符合用户偏好
- [ ] Publish mode is confirmed: draft or publish / 已确认发布方式：草稿或正式发布
```

Use a locally configured WeChat publisher adapter for the actual WeChat operation. Prefer draft creation unless the user explicitly asks to publish.

实际微信操作使用本地配置的 WeChat publisher adapter。除非用户明确要求正式发布，否则默认只创建草稿。
