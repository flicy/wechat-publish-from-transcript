import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_public_ready.py"


def load_module():
    spec = importlib.util.spec_from_file_location("check_public_ready", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["check_public_ready"] = module
    spec.loader.exec_module(module)
    return module


class PublicReadyCheckTest(unittest.TestCase):
    def test_clean_bilingual_skill_package_passes(self):
        checker = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text("# 标题\n\nEnglish section\n")
            (root / "README.md").write_text("# 中文\n\nEnglish\n")
            issues = checker.collect_public_ready_issues(root)
        self.assertEqual([], issues)

    def test_private_publisher_name_is_reported(self):
        checker = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text("# 标题\n\nEnglish section\n")
            (root / "README.md").write_text("private " + "b" + "aoyu" + " adapter\n")
            issues = checker.collect_public_ready_issues(root)
        self.assertTrue(any(issue.kind == "blocked-text" for issue in issues))

    def test_markdown_without_bilingual_content_is_reported(self):
        checker = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("English only\n")
            issues = checker.collect_public_ready_issues(root)
        self.assertTrue(any(issue.kind == "markdown-language" for issue in issues))


if __name__ == "__main__":
    unittest.main()
