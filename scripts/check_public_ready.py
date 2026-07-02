#!/usr/bin/env python3
"""Check whether the skill package is safe to publish publicly."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


BLOCKED_TEXT = [
    "b" + "aoyu",
    "宝" + "玉",
    "post" + "-to-" + "wechat",
    "BAO" + "YU",
    "BAO" + "_YU",
    "Growth" + "OS",
    "/" + "Users/",
]

SKIP_DIRS = {".git", "__pycache__", "node_modules"}


@dataclass(frozen=True)
class Issue:
    kind: str
    path: str
    detail: str


def has_chinese(text: str) -> bool:
    return any("\u4e00" <= ch <= "\u9fff" for ch in text)


def has_english(text: str) -> bool:
    return any(("A" <= ch <= "Z") or ("a" <= ch <= "z") for ch in text)


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file():
            yield path


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(errors="ignore")
    except OSError:
        return None


def collect_public_ready_issues(root: Path) -> list[Issue]:
    root = root.resolve()
    issues: list[Issue] = []

    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()

        if path.name == ".DS_Store":
            issues.append(Issue("junk-file", rel, "remove macOS metadata file"))
            continue

        text = read_text(path)
        if text is None:
            issues.append(Issue("read-error", rel, "could not read file"))
            continue

        for pattern in BLOCKED_TEXT:
            if pattern in text:
                issues.append(Issue("blocked-text", rel, f"contains blocked public reference: {pattern}"))

        if path.suffix.lower() == ".md" and not (has_chinese(text) and has_english(text)):
            issues.append(Issue("markdown-language", rel, "Markdown must include Chinese and English content"))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", type=Path)
    args = parser.parse_args()

    issues = collect_public_ready_issues(args.root)
    if issues:
        for issue in issues:
            print(f"{issue.kind}: {issue.path}: {issue.detail}")
        return 1

    print("public-ready check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
