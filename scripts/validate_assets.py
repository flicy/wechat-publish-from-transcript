#!/usr/bin/env python3
"""Validate image files and dimensions for a publish run."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--min-width", type=int, default=600)
    parser.add_argument("--min-height", type=int, default=600)
    parser.add_argument("--ratio", type=float, help="Required width/height ratio, for example 2.35 for WeChat cover.")
    parser.add_argument("--ratio-tolerance", type=float, default=0.03)
    args = parser.parse_args()

    failed = False
    for path in args.paths:
        if not path.exists():
            print(f"missing\t{path}")
            failed = True
            continue
        try:
            with Image.open(path) as img:
                width, height = img.size
        except Exception as exc:
            print(f"invalid\t{path}\t{exc}")
            failed = True
            continue

        status = "ok" if width >= args.min_width and height >= args.min_height else "small"
        ratio_note = ""
        if args.ratio:
            actual_ratio = width / height
            ratio_note = f"\tratio={actual_ratio:.3f}"
            if abs(actual_ratio - args.ratio) > args.ratio_tolerance:
                status = "bad-ratio"
        print(f"{status}\t{width}x{height}\t{path}")
        if ratio_note:
            print(f"ratio-check\ttarget={args.ratio:.3f}\ttolerance={args.ratio_tolerance:.3f}{ratio_note}")
        if status != "ok":
            failed = True

    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
