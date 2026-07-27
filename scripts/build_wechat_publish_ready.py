#!/usr/bin/env python3
"""Build a WeChat publish-ready markdown file from a transcript run directory.

Topic-agnostic. Image mapping is dynamic: each ``<!-- 图片 NN ... -->`` placeholder
is matched to an image in ``assets/final/wechat/`` whose filename starts with the
same zero-padded index (e.g. ``图片 02`` -> ``02-*.png``). Alt text comes from an
optional inline hint (``<!-- 图片 02 三种方法 -->``) or is derived from the slug.
A referenced image that is missing is a HARD ERROR (exit 1), never a silent skip.

Index 01 is reserved for the cover (emitted as frontmatter ``coverImage``, not
inline). A ``<!-- CTA -->`` marker, if present, is replaced with the community QR
image (``--cta`` path, or auto-discovered as ``*cta*`` in the wechat image dir).
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp")


def humanize_slug(filename: str) -> str:
    stem = Path(filename).stem
    stem = re.sub(r"^\d+[-_]?", "", stem)  # strip leading index like "02-"
    return stem.replace("-", " ").replace("_", " ").strip() or filename


def find_image_by_index(image_dir: Path, index: int) -> Path | None:
    """Match an image whose stem equals NN or starts with NN- / NN_."""
    if not image_dir.is_dir():
        return None
    prefix = f"{index:02d}"
    for f in sorted(image_dir.iterdir()):
        if f.suffix.lower() not in IMAGE_EXTS:
            continue
        if f.stem == prefix or f.stem.startswith(prefix + "-") or f.stem.startswith(prefix + "_"):
            return f
    return None


def read_front_title(article: str) -> str:
    match = re.search(r"^#\s+(.+)$", article, re.MULTILINE)
    return match.group(1).strip() if match else "未命名文章"


def read_summary(article: str) -> str:
    quote = re.search(r"^>\s+(.*)$", article, re.MULTILINE)
    if quote:
        return quote.group(1).strip()[:120]
    for line in article.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("!") and not line.startswith("<!--"):
            return line[:120]
    return ""


def relpath(target: Path, base: Path) -> str:
    return Path(os.path.relpath(target, base)).as_posix()


def replace_image_comments(article: str, image_dir: Path, md_dir: Path,
                           cover_index: int, missing: list[str]) -> str:
    def repl(match: re.Match[str]) -> str:
        index = int(match.group(1))
        hint = (match.group(2) or "").strip()
        if index == cover_index:
            return ""  # cover is emitted in frontmatter, not inline
        img = find_image_by_index(image_dir, index)
        if img is None:
            missing.append(f"图片 {index:02d}（assets/final/wechat/ 里没有 {index:02d}-* 图）")
            return match.group(0)
        alt = hint or humanize_slug(img.name)
        return f"![{alt}]({relpath(img, md_dir)})"

    return re.sub(r"<!--\s*图片\s+(\d+)\s*(.*?)-->", repl, article)


def insert_cta(article: str, image_dir: Path, md_dir: Path, cta_arg: str | None) -> str:
    if "<!-- CTA -->" not in article:
        return article
    cta: Path | None = Path(cta_arg) if cta_arg else None
    if cta is None and image_dir.is_dir():
        cands = sorted(p for p in image_dir.iterdir()
                       if "cta" in p.stem.lower() and p.suffix.lower() in IMAGE_EXTS)
        cta = cands[0] if cands else None
    if cta is None or not cta.exists():
        return article.replace("<!-- CTA -->", "")
    return article.replace("<!-- CTA -->", f"![社群二维码]({relpath(cta, md_dir)})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--article", default="article-publish.md")
    parser.add_argument("--out", default="wechat/publish-ready.md")
    parser.add_argument("--author", default="Publisher")
    parser.add_argument("--title")
    parser.add_argument("--summary")
    parser.add_argument("--cover-index", type=int, default=1,
                        help="image index reserved for the cover (default 1)")
    parser.add_argument("--cta", help="explicit community QR image path for <!-- CTA -->")
    args = parser.parse_args()

    run_dir = args.run_dir.resolve()
    article_path = run_dir / args.article
    out_path = run_dir / args.out
    md_dir = out_path.parent
    md_dir.mkdir(parents=True, exist_ok=True)
    image_dir = run_dir / "assets" / "final" / "wechat"

    if not article_path.exists():
        raise SystemExit(f"Article not found: {article_path}")

    article = article_path.read_text(encoding="utf-8")

    missing: list[str] = []
    article = replace_image_comments(article, image_dir, md_dir, args.cover_index, missing)
    article = insert_cta(article, image_dir, md_dir, args.cta)

    if missing:
        sys.stderr.write("❌ 以下占位图缺失，无法生成 publish-ready：\n")
        for m in missing:
            sys.stderr.write(f"   • {m}\n")
        raise SystemExit(1)

    cover = find_image_by_index(image_dir, args.cover_index)
    if cover is None:
        raise SystemExit(
            f"Missing cover image: no {args.cover_index:02d}-* image in {image_dir}")

    title = args.title or read_front_title(article)
    summary = args.summary or read_summary(article)
    frontmatter = (
        "---\n"
        f'title: "{title}"\n'
        f'author: "{args.author}"\n'
        f'summary: "{summary}"\n'
        f'coverImage: "{relpath(cover, md_dir)}"\n'
        "---\n\n"
    )
    out_path.write_text(frontmatter + article, encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()
