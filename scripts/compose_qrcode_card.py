#!/usr/bin/env python3
"""Compose a real QR code onto an existing image card."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def load_font(size: int) -> ImageFont.ImageFont:
    for candidate in [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ]:
        try:
            return ImageFont.truetype(candidate, size)
        except Exception:
            pass
    return ImageFont.load_default()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--qr", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--x", type=int, required=True)
    parser.add_argument("--y", type=int, required=True)
    parser.add_argument("--size", type=int, default=220)
    parser.add_argument("--label", default="扫码关注公众号")
    args = parser.parse_args()

    base = Image.open(args.base).convert("RGBA")
    qr = Image.open(args.qr).convert("RGB")
    qr = qr.resize((args.size, args.size), Image.Resampling.NEAREST).convert("RGBA")

    padding = 18
    label_h = 38
    card_w = args.size + padding * 2
    card_h = args.size + padding * 2 + label_h
    x, y = args.x, args.y

    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle((x + 8, y + 10, x + card_w + 8, y + card_h + 10), radius=18, fill=(0, 0, 0, 45))
    base = Image.alpha_composite(base, shadow)

    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle((x, y, x + card_w, y + card_h), radius=18, fill=(255, 252, 244, 255), outline=(215, 205, 188, 255), width=3)
    draw.rectangle((x + padding - 4, y + padding - 4, x + padding + args.size + 4, y + padding + args.size + 4), fill=(255, 255, 255, 255))
    base.alpha_composite(qr, (x + padding, y + padding))

    font = load_font(24)
    text_box = draw.textbbox((0, 0), args.label, font=font)
    text_w = text_box[2] - text_box[0]
    draw.text((x + (card_w - text_w) / 2, y + padding + args.size + 10), args.label, fill=(20, 20, 20, 255), font=font)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    base.convert("RGB").save(args.out, quality=96)
    print(args.out)


if __name__ == "__main__":
    main()
