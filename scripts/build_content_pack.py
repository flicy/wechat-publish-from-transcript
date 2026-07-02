#!/usr/bin/env python3
"""Build a starter social-pack/content-pack.json."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def read(path: Path | None) -> str:
    if not path:
        return ""
    return path.read_text(encoding="utf-8") if path.exists() else ""


def extract_title(markdown: str) -> str:
    fm = re.search(r"^---\n(.*?)\n---", markdown, re.S)
    if fm:
        m = re.search(r"^title:\s*(.+)$", fm.group(1), re.M)
        if m:
            return m.group(1).strip().strip('"')
    m = re.search(r"^#\s+(.+)$", markdown, re.M)
    return m.group(1).strip() if m else ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article", type=Path)
    parser.add_argument("--highlights", type=Path)
    parser.add_argument("--out", type=Path, default=Path("social-pack/content-pack.json"))
    parser.add_argument("--wechat-url", default="")
    args = parser.parse_args()

    article = read(args.article)
    highlights = read(args.highlights)
    highlight_titles = re.findall(r"^Candidate title:\s*(.+)$", highlights, re.M)

    data = {
        "title": extract_title(article),
        "summary": "",
        "source_url": "",
        "wechat_url": args.wechat_url,
        "audience": "",
        "highlight_method": {
            "source": "transcript",
            "scoring_dimensions": [
                "hook",
                "information_density",
                "practical_value",
                "story",
                "novelty",
                "quoteability",
                "standalone_completeness",
                "visual_potential",
                "platform_interaction_signal",
                "risk_control",
            ],
        },
        "highlights": [
            {
                "id": f"h{i:02d}",
                "timestamp": "",
                "title": title,
                "score": 0,
                "reason": "",
                "platform_signals": [],
                "platform_source": "none",
                "evidence_excerpt": "",
                "quote_candidates": [],
                "image_task": "",
            }
            for i, title in enumerate(highlight_titles, start=1)
        ],
        "chapters": [],
        "cta": {"wechat": "", "community": "", "qrcode_image": ""},
        "xiaohongshu": {
            "post_path": "xiaohongshu/post.md",
            "card_sequence_path": "xiaohongshu/card-sequence.md",
            "cards": [],
        },
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(args.out)


if __name__ == "__main__":
    main()
