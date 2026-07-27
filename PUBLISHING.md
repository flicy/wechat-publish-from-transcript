# Publishing Guide / 发布指南

## 中文

### 发布前检查

在公开前，从仓库根目录运行这些命令：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
python3 scripts/check_public_ready.py .
python3 scripts/component_lint.py
bash -n scripts/submit_wechat_draft.sh
python3 -m unittest discover -s tests
```

预期结果：

- Skill 验证打印 `Skill is valid!`
- 公开就绪检查打印 `public-ready check passed`。
- 组件库检查打印 `全部组件库源头无反模式`。
- Shell 语法检查没有输出并成功退出。
- 单元测试打印 `OK`。

### 创建 GitHub 仓库并推送

如果 GitHub CLI 已认证，创建公开仓库并推送：

```bash
gh auth status
gh repo create wechat-publish-from-transcript --public --source . --remote origin --push
```

如果已经创建空 GitHub 仓库：

```bash
git remote add origin https://github.com/<owner>/wechat-publish-from-transcript.git
git push -u origin main
```

把 `<owner>` 替换成你的 GitHub 用户名或组织。

### 发布后检查

发布后确认：

- GitHub 首页渲染 `README.md`。
- `SKILL.md`、`references/`、`scripts/`、`assets/` 和 `agents/` 已上传。
- 仓库不含秘密、cookie、token、二维码源图片或个人发布者名字。
- 如果其他人应该被允许复用该包，选择并添加许可文件，例如 MIT、Apache-2.0 或你批准的许可。

## English

### Pre-Publish Checks

Before publishing publicly, run these commands from the repository root:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
python3 scripts/check_public_ready.py .
python3 scripts/component_lint.py
bash -n scripts/submit_wechat_draft.sh
python3 -m unittest discover -s tests
```

Expected results:

- Skill validation prints `Skill is valid!`.
- Public readiness check prints `public-ready check passed`.
- Component lint prints that all component libraries are clean.
- Shell syntax check prints nothing and exits successfully.
- Unit tests print `OK`.

### Create The GitHub Repository And Push

If GitHub CLI is authenticated, create a public repository and push directly:

```bash
gh auth status
gh repo create wechat-publish-from-transcript --public --source . --remote origin --push
```

If you already created an empty GitHub repository:

```bash
git remote add origin https://github.com/<owner>/wechat-publish-from-transcript.git
git push -u origin main
```

Replace `<owner>` with your GitHub username or organization.

### Post-Publish Checks

After publishing, confirm:

- GitHub renders `README.md` on the repository home page.
- `SKILL.md`, `references/`, `scripts/`, `assets/`, and `agents/` are uploaded.
- The repository contains no secrets, cookies, tokens, QR source images, or personal publisher names.
- If others should be allowed to reuse the package, choose and add a license file, such as MIT, Apache-2.0, or another license you approve.
