#!/usr/bin/env python3
"""Smoke tests for the typesetting layer.

Covers the dual-gate validators (validate_gzh_html dynamic gate, component_lint
static gate) and the topic-agnostic publish-ready builder (dynamic image
matching + hard error on missing images).
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import validate_gzh_html  # noqa: E402

GOOD_HTML = (
    '<section style="max-width:677px"><p style="font-size:15px">'
    '<span leaf="">这是被正确包裹的中文。</span></p></section>'
)
BAD_HTML = '<div class="x"><style>.a{color:red}</style>没有包裹的中文</div>'


class ValidateGzhHtmlTest(unittest.TestCase):
    def test_good_html_passes(self):
        errors, _warnings, leaf = validate_gzh_html.validate(GOOD_HTML)
        self.assertEqual(errors, [])
        self.assertGreater(leaf, 0)

    def test_bad_html_errors(self):
        errors, _warnings, _leaf = validate_gzh_html.validate(BAD_HTML)
        self.assertTrue(errors)  # div / class / style / missing span leaf

    def test_cjk_without_leaf_is_error(self):
        errors, _w, _l = validate_gzh_html.validate("<section><p>裸中文</p></section>")
        self.assertTrue(any("span leaf" in e for e in errors))


class ComponentLintTest(unittest.TestCase):
    def test_theme_libraries_are_clean(self):
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS / "component_lint.py")],
            cwd=REPO_ROOT, capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)


class PublishReadyBuilderTest(unittest.TestCase):
    def _fixture(self, root: Path) -> None:
        img = root / "assets" / "final" / "wechat"
        img.mkdir(parents=True)
        for name in ("01-cover.png", "02-methods.png"):
            (img / name).write_bytes(b"x")
        (root / "article-publish.md").write_text(
            "# 标题\n\n> 摘要一句话。\n\n正文段落。\n\n<!-- 图片 02 方法图 -->\n",
            encoding="utf-8")

    def _build(self, root: Path) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(SCRIPTS / "build_wechat_publish_ready.py"),
             "--run-dir", str(root)], capture_output=True, text=True)

    def test_dynamic_image_matching(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._fixture(root)
            proc = self._build(root)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            out = (root / "wechat" / "publish-ready.md").read_text(encoding="utf-8")
            self.assertIn("![方法图](", out)  # alt from inline hint
            self.assertIn("02-methods.png", out)
            self.assertIn('coverImage: "../assets/final/wechat/01-cover.png"', out)

    def test_missing_image_is_hard_error(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._fixture(root)
            (root / "article-publish.md").write_text(
                "# 标题\n\n正文段落。\n\n<!-- 图片 09 -->\n", encoding="utf-8")
            proc = self._build(root)
            self.assertEqual(proc.returncode, 1)


if __name__ == "__main__":
    unittest.main()
