#!/usr/bin/env python3
"""Build a Xiaohongshu post draft from social-pack/content-pack.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def first_nonempty(*values: object) -> str:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def pick_highlights(data: dict, limit: int = 5) -> list[dict]:
    highlights = data.get("highlights") or []
    return sorted(highlights, key=lambda item: item.get("score", 0), reverse=True)[:limit]


def format_tags(data: dict) -> str:
    audience = first_nonempty(data.get("audience"))
    base_tags = ["#AI工具", "#公众号运营", "#小红书图文", "#内容复盘"]
    if "增长" in audience:
        base_tags.append("#AI增长")
    if "开发" in audience or "Coding" in audience:
        base_tags.append("#VibeCoding")
    return " ".join(dict.fromkeys(base_tags))


def build_post(data: dict) -> str:
    title = first_nonempty(data.get("title"), "这场分享，最值得带走的几件事")
    summary = first_nonempty(data.get("summary"), "我把这场分享整理成了几个可执行的重点，适合收藏后慢慢看。")
    highlights = pick_highlights(data)
    cta = data.get("cta") or {}
    cta_text = first_nonempty(
        cta.get("community"),
        cta.get("wechat"),
        "想看完整复盘，可以继续关注后续文章和活动。",
    )

    lines = [
        "# Xiaohongshu Post / 小红书帖子",
        "",
        "## 标题 / Title",
        "",
        title[:28],
        "",
        "## 正文 / Body",
        "",
        summary,
        "",
        "这次最值得收藏的是：",
        "",
    ]

    if highlights:
        for index, item in enumerate(highlights, start=1):
            item_title = first_nonempty(item.get("title"), f"重点 {index}")
            reason = first_nonempty(item.get("reason"), item.get("evidence_excerpt"))
            lines.append(f"{index}. {item_title}")
            if reason:
                lines.append(f"   {reason[:80]}")
    else:
        lines.extend([
            "1. 先把逐字稿里最有信息密度的片段找出来",
            "2. 再把每个片段变成一张能看懂的图卡",
            "3. 最后沉淀成公众号、小红书和 X 都能复用的内容包",
        ])

    lines.extend([
        "",
        cta_text,
        "",
        "## 话题标签 / Hashtags",
        "",
        format_tags(data),
        "",
        "## 图卡顺序 / Card Sequence",
        "",
        "1. 封面：最强钩子 + 核心视觉",
        "2. 背景：这场分享为什么值得看",
        "3. 洞察：最反常识或最有用的判断",
        "4. 方法：可执行流程/清单",
        "5. 案例：真实故事或项目结果",
        "6. 延伸：工具、风险或适用人群",
        "7. 总结/CTA：关注、社群或下期活动",
        "",
        "## 生成说明 / Generation Notes",
        "",
        "- This draft is built from `social-pack/content-pack.json` only.",
        "- It is designed for token-saving parallel execution and should not require re-reading the full transcript.",
        "- 图片和二维码仍需按 `references/image-style.md` 使用真实文件和最终图卡。",
    ])

    return "\n".join(lines) + "\n"


def build_card_sequence(data: dict) -> str:
    title = first_nonempty(data.get("title"), "小红书图文笔记")
    highlights = pick_highlights(data)
    roles = [
        ("封面", "最强钩子 + 核心视觉"),
        ("背景", "这场内容为什么值得看"),
        ("洞察", "最反常识或最有价值的判断"),
        ("方法", "流程、清单或操作步骤"),
        ("案例", "真实故事、项目或结果"),
        ("延伸", "工具、风险或适用人群"),
        ("总结/CTA", "关注、社群或下期活动"),
    ]
    lines = [
        "# Xiaohongshu Card Sequence / 小红书图卡顺序",
        "",
        f"主题 / Topic: {title}",
        "",
    ]
    for index, (role, default_desc) in enumerate(roles, start=1):
        item = highlights[index - 2] if index >= 2 and index - 2 < len(highlights) else {}
        card_title = first_nonempty(item.get("title"), default_desc)
        lines.append(f"{index}. {role}: {card_title}")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--content-pack", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--cards-out", type=Path)
    args = parser.parse_args()

    data = load_json(args.content_pack)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(build_post(data), encoding="utf-8")
    cards_out = args.cards_out or args.out.with_name("card-sequence.md")
    cards_out.parent.mkdir(parents=True, exist_ok=True)
    cards_out.write_text(build_card_sequence(data), encoding="utf-8")
    print(args.out)
    print(cards_out)


if __name__ == "__main__":
    main()
