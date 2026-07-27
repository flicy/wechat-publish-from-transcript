# WeChat Preflight Checklist / 微信发布预检

Before creating a WeChat draft or publishing, create `wechat/preview-checklist.md`.

每次微信草稿提交前，生成 `wechat/preview-checklist.md`。

```md
# WeChat Preview Checklist / 微信预览预检清单

- [ ] Title has no typo / 标题没有错字
- [ ] Summary is concise and platform-safe / 摘要简洁且平台安全
- [ ] Cover exists and displays correctly / 封面存在且显示正确
- [ ] First WeChat image is `assets/final/wechat/01-cover.png` and uses `2.35:1` ratio / 微信第一张图是 `2.35:1` 封面图
- [ ] Key title/subject stays in the central safe area / 标题和主体留在中央安全区
- [ ] Article title block accent color matches the generated image accent color / 文章标题块强调色和生成图片强调色一致
- [ ] Title block uses screenshot style: left accent bar, pale background, dark text / 标题块使用截图式左强调条、浅底、深墨文字的截图风格
- [ ] Body is typeset into `wechat/article.html` (flat `<section>` + inline styles) / 正文已排版成 `wechat/article.html`
- [ ] `python3 scripts/validate_gzh_html.py wechat/article.html` passes with 0 ERROR / 排版校验 0 ERROR
- [ ] One theme only, no mixing; all Chinese wrapped in `<span leaf="">` / 一篇文章一个主题，中文均用 `<span leaf="">` 包裹
- [ ] Inline images exist and display correctly / 内嵌图存在且显示正确
- [ ] WeChat inline chapter images are landscape 16:9 or near 16:9 / 微信内嵌章节图是横图 16:9 或近 16:9
- [ ] Xiaohongshu 3:4 vertical cards are not mixed into WeChat body / 不把小红书 3:4 竖版卡片混入微信正文
- [ ] Image text has no obvious typo / 图片文字没有明显错字
- [ ] Image title/subtitle scale follows `references/image-style.md` / 图片标题和副标题比例遵循参考图规范
- [ ] Main illustration/diagram is visually heavier than the headline on explanation images / 说明图的主插图/图表比标题更重
- [ ] `00-overview-recap` explains the whole session with evidence-backed people, topics, questions, tools, and conclusions / 总览图用证据支撑人物、主题、问题和结论
- [ ] `image-prompts.md` exists and includes unified master prompt plus WeChat/Xiaohongshu per-image prompts / 输出统一 Prompt 和每图 Prompt
- [ ] Chapter explanation images match final highlights / 章节说明图匹配最终亮点
- [ ] Each image explains one idea / 每张图解释一个观点
- [ ] Xiaohongshu cards are 3:4 vertical, clear, light, and easy to understand / 小红书卡片是 3:4，清晰、不累、易懂
- [ ] Official Account QR code uses the real provided file if used / 如果使用公众号二维码，用真实文件
- [ ] Community QR code uses the real provided file if used / 如果使用社群二维码，用真实文件
- [ ] Speaker names are correct / 讲者名字正确
- [ ] Event issue, date, and activity name are correct / 期数、日期、活动名正确
- [ ] Claims and quotes are supported by transcript evidence / 主张和引用有转写稿证据
- [ ] No AppSecret or private credentials appear in output files / 输出文件不含 AppSecret 或私密凭证
- [ ] Source URL / 来源链接 is correct if used / 如果使用来源链接，确认正确
- [ ] Comment settings match user preference / 评论设置符合用户偏好
- [ ] Publish mode is confirmed: draft or publish / 确认发布模式：草稿或发布
```

Use a locally configured WeChat publisher adapter for the actual WeChat operation. Prefer draft creation unless the user explicitly asks to publish.

最终微信操作使用本地配置的 WeChat publisher adapter。默认创建草稿，除非用户明确要求发布。
