#!/usr/bin/env python3
"""Create a starter highlight candidate file from a transcript.

This is a heuristic scaffold. The agent must review and edit the result.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TIMESTAMP_RE = re.compile(r"(?P<ts>(?:\d{1,2}:)?\d{1,2}:\d{2})(?:\s*[-–—]\s*(?P<end>(?:\d{1,2}:)?\d{1,2}:\d{2}))?")


def split_timestamped(text: str, min_chars: int) -> list[tuple[str, str]]:
    matches = list(TIMESTAMP_RE.finditer(text))
    if not matches:
        return []

    chunks: list[tuple[str, str]] = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        timestamp = match.group("ts")
        chunk = text[start:end].strip()
        if len(chunk) >= min_chars:
            chunks.append((timestamp, chunk))
    return chunks


def split_paragraphs(text: str, min_chars: int) -> list[tuple[str, str]]:
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks: list[tuple[str, str]] = []
    buffer: list[str] = []
    count = 0

    for para in paras:
        buffer.append(para)
        count += len(para)
        if count >= 900:
            chunks.append(("missing_timestamp", "\n\n".join(buffer)))
            buffer = []
            count = 0

    if buffer:
        chunk = "\n\n".join(buffer)
        if len(chunk) >= min_chars:
            chunks.append(("missing_timestamp", chunk))
    return chunks


def title_from_chunk(chunk: str) -> str:
    clean = re.sub(r"\s+", " ", chunk)
    clean = TIMESTAMP_RE.sub("", clean).strip()
    for sep in ["。", "！", "？", ".", "!", "?"]:
        if sep in clean:
            clean = clean.split(sep, 1)[0]
            break
    return clean[:36] or "待命名高光"


def excerpt(chunk: str, limit: int = 180) -> str:
    clean = re.sub(r"\s+", " ", chunk).strip()
    return clean[:limit] + ("..." if len(clean) > limit else "")


def build_markdown(chunks: list[tuple[str, str]], max_items: int) -> str:
    lines = ["# Highlight Candidates", "", "> Heuristic scaffold. Review and score manually.", ""]
    for idx, (timestamp, chunk) in enumerate(chunks[:max_items], start=1):
        hid = f"h{idx:02d}"
        lines.extend(
            [
                f"## {hid}",
                "",
                f"Timestamp: {timestamp}",
                f"Candidate title: {title_from_chunk(chunk)}",
                "Use: TBD",
                "Reason: TBD",
                f"Evidence excerpt: {excerpt(chunk)}",
                "Quote candidates:",
                "- TBD",
                "Image task: pain_point | insight | method | workflow | case | summary",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("transcript", type=Path)
    parser.add_argument("--out", type=Path, default=Path("highlight-candidates.md"))
    parser.add_argument("--max-items", type=int, default=12)
    parser.add_argument("--min-chars", type=int, default=40)
    args = parser.parse_args()

    text = args.transcript.read_text(encoding="utf-8")
    chunks = split_timestamped(text, args.min_chars) or split_paragraphs(text, args.min_chars)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(build_markdown(chunks, args.max_items), encoding="utf-8")
    print(args.out)


if __name__ == "__main__":
    main()
