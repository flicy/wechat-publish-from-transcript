#!/usr/bin/env python3
"""Build a WeChat publish-ready markdown file from a transcript run directory."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


IMAGE_BY_COMMENT_HINT = {
    "配图 00": "00-overview-recap.png",
    "配图 01": None,
    "配图 02": "02-three-methods.png",
    "配图 03": "03-comment-capture.png",
    "配图 04": "04-geo-network.png",
    "配图 05": "05-geo-workflow.png",
    "配图 06": "06-kol-funnel.png",
    "配图 07": "07-platform-choice.png",
    "配图 08": "08-mvp-validation.png",
    "配图 09": "09-multidimensional-competition.png",
    "配图 10": "10-feedback-flywheel.png",
    "配图 11": "11-community-cta.png",
}


ALT_BY_IMAGE = {
    "00-overview-recap.png": "总回顾：一图读懂本场讨论",
    "02-three-methods.png": "出海增长三板斧",
    "03-comment-capture.png": "评论区获客",
    "04-geo-network.png": "GEO：让 AI 更容易引用你",
    "05-geo-workflow.png": "GEO 不是玄学",
    "06-kol-funnel.png": "红人营销漏斗",
    "07-platform-choice.png": "平台选择",
    "08-mvp-validation.png": "MVP 验证",
    "09-multidimensional-competition.png": "避开单一维度竞争",
    "10-feedback-flywheel.png": "反馈闭环",
    "11-community-cta.png": "社群活动说明",
}


def read_front_title(article: str) -> str:
    match = re.search(r"^#\s+(.+)$", article, re.MULTILINE)
    return match.group(1).strip() if match else "未命名文章"


def read_summary(article: str) -> str:
    quote = re.search(r"^>\s+(.+)$", article, re.MULTILINE)
    if quote:
        return quote.group(1).strip()[:120]
    for line in article.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("!") and not line.startswith("<!--"):
            return line[:120]
    return ""


def replace_image_comments(article: str, run_dir: Path, md_dir: Path) -> str:
    image_dir = run_dir / "assets" / "final" / "wechat"

    def repl(match: re.Match[str]) -> str:
        comment = match.group(0)
        for hint, filename in IMAGE_BY_COMMENT_HINT.items():
            if hint in comment:
                if filename is None:
                    return ""
                image_path = image_dir / filename
                if not image_path.exists():
                    return comment
                rel = image_path.relative_to(md_dir) if image_path.is_relative_to(md_dir) else Path("..") / image_path.relative_to(run_dir)
                alt = ALT_BY_IMAGE.get(filename, filename)
                return f"![{alt}]({rel.as_posix()})"
        return comment

    return re.sub(r"<!--\s*配图\s+\d+.*?-->", repl, article)


def maybe_insert_cta(article: str, run_dir: Path, md_dir: Path) -> str:
    cta = run_dir / "assets" / "final" / "wechat" / "11-community-cta.png"
    if not cta.exists() or "11-community-cta.png" in article:
        return article
    marker = "如果你也在做 AI 产品、出海增长、独立开发，或者只是有一个想验证的想法，欢迎继续关注后续活动。"
    if marker not in article:
        return article
    rel = Path("..") / cta.relative_to(run_dir)
    return article.replace(marker, f"![社群活动说明]({rel.as_posix()})\n\n{marker}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--article", default="article-publish.md")
    parser.add_argument("--out", default="wechat/publish-ready.md")
    parser.add_argument("--author", default="Publisher")
    parser.add_argument("--title")
    parser.add_argument("--summary")
    args = parser.parse_args()

    run_dir = args.run_dir.resolve()
    article_path = run_dir / args.article
    out_path = run_dir / args.out
    md_dir = out_path.parent
    md_dir.mkdir(parents=True, exist_ok=True)

    article = article_path.read_text()
    article = replace_image_comments(article, run_dir, md_dir)
    article = maybe_insert_cta(article, run_dir, md_dir)

    cover = run_dir / "assets" / "final" / "wechat" / "01-cover.png"
    if not cover.exists():
        raise SystemExit(f"Missing cover image: {cover}")
    cover_rel = Path("..") / cover.relative_to(run_dir)

    title = args.title or read_front_title(article)
    summary = args.summary or read_summary(article)
    frontmatter = (
        "---\n"
        f'title: "{title}"\n'
        f'author: "{args.author}"\n'
        f'summary: "{summary}"\n'
        f'coverImage: "{cover_rel.as_posix()}"\n'
        "---\n\n"
    )
    out_path.write_text(frontmatter + article)
    print(out_path)


if __name__ == "__main__":
    main()
