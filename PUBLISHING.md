# Publishing Guide / 发布指南

## 中文

### 发布前检查

在公开发布前，从仓库根目录运行：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
python3 scripts/check_public_ready.py .
bash -n scripts/submit_wechat_draft.sh
python3 -m unittest discover -s tests
```

期望结果：

- Skill 校验输出 `Skill is valid!`
- 公开发布检查输出 `public-ready check passed`。
- Shell 语法检查无输出并返回成功。
- 单元测试输出 `OK`。

### 创建 GitHub 仓库并推送

如果 GitHub CLI 已登录，可以直接创建公开仓库并推送：

```bash
gh auth status
gh repo create wechat-publish-from-transcript --public --source . --remote origin --push
```

如果已经在 GitHub 上创建了空仓库：

```bash
git remote add origin git@github.com:<owner>/wechat-publish-from-transcript.git
git push -u origin main
```

把 `<owner>` 替换成你的 GitHub 用户名或组织名。

### 发布后检查

发布后确认：

- GitHub 首页能看到 `README.md`。
- `SKILL.md`、`references/`、`scripts/`、`assets/` 和 `agents/` 都已上传。
- 仓库中没有密钥、Cookie、Token、二维码原图或个人发布器名称。
- 如需允许他人复用，选择并添加许可证文件，例如 MIT、Apache-2.0 或其他你认可的许可证。

## English

### Pre-Publish Checks

Before publishing publicly, run these commands from the repository root:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
python3 scripts/check_public_ready.py .
bash -n scripts/submit_wechat_draft.sh
python3 -m unittest discover -s tests
```

Expected results:

- Skill validation prints `Skill is valid!`.
- Public readiness check prints `public-ready check passed`.
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
git remote add origin git@github.com:<owner>/wechat-publish-from-transcript.git
git push -u origin main
```

Replace `<owner>` with your GitHub username or organization.

### Post-Publish Checks

After publishing, confirm:

- GitHub renders `README.md` on the repository home page.
- `SKILL.md`, `references/`, `scripts/`, `assets/`, and `agents/` are uploaded.
- The repository contains no secrets, cookies, tokens, QR source images, or personal publisher names.
- If others should be allowed to reuse the package, choose and add a license file, such as MIT, Apache-2.0, or another license you approve.
