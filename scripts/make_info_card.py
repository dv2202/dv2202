#!/usr/bin/env python3
"""Build a neofetch-style info card SVG.

Usage:
    python scripts/make_info_card.py          # animated
    STATIC=1 python scripts/make_info_card.py  # frozen frame

Output: info-card.svg
"""

import os
from pathlib import Path

STATIC = os.environ.get("STATIC", "0") == "1"

TITLE = "devansh@github"
BANNER_COLOR = "#58a6ff"
BG_COLOR = "#0d1117"
TEXT_COLOR = "#c9d1d9"
LABEL_COLOR = "#8b949e"
ACCENT = "#58a6ff"
BORDER_COLOR = "#30363d"

WIDTH = 490
PAD = 20
TITLE_H = 32
ROW_H = 26
ROW_GAP = 6
CORNER_R = 6

ROWS = [
    ("Title", "Software Developer @ ForestAi"),
    ("Now", "Building with C++, Python & Web"),
    ("Prev", "Open Source Contributor"),
    ("Stack", "C/C++  ·  React  ·  Tailwind  ·  MongoDB"),
    ("Highlights", "9k+ contributions & counting"),
]

LABEL_COLORS = ["#58a6ff", "#f0883e", "#8b949e", "#3fb950", "#bc8cff"]


def main():
    total_h = PAD + TITLE_H + len(ROWS) * (ROW_H + ROW_GAP) + PAD
    parts = []

    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {total_h}" width="{WIDTH}" height="{total_h}">')
    parts.append(f'<rect width="{WIDTH}" height="{total_h}" rx="{CORNER_R}" fill="{BG_COLOR}" stroke="{BORDER_COLOR}" stroke-width="1"/>')

    if not STATIC:
        parts.append("<style>")
        for i in range(len(ROWS)):
            d = i * 0.12
            parts.append(f"@keyframes row{i}{{0%{{opacity:0;transform:translateX(8px)}}100%{{opacity:1;transform:translateX(0)}}}}")
            parts.append(f".row{i}{{animation:row{i} 0.5s ease-out {d}s both}}")
        parts.append("@keyframes titleFade{0%{opacity:0}100%{opacity:1}}")
        parts.append(f".title{{animation:titleFade 0.4s ease-out both}}")
        parts.append("</style>")

    cls = " class=\"title\"" if not STATIC else ""
    parts.append(
        f'<text x="{PAD}" y="{PAD + 22}" font-family="Consolas,Monaco,monospace" '
        f'font-size="15" font-weight="bold" fill="{ACCENT}"{cls}>'
        f"~/{TITLE}</text>"
    )

    parts.append(f'<line x1="{PAD}" y1="{PAD + TITLE_H}" x2="{WIDTH - PAD}" y2="{PAD + TITLE_H}" stroke="{BORDER_COLOR}" stroke-width="1"/>')

    for i, (label, value) in enumerate(ROWS):
        y = PAD + TITLE_H + ROW_GAP + i * (ROW_H + ROW_GAP) + 20
        anim_cls = f" class=\"row{i}\"" if not STATIC else ""
        lcolor = LABEL_COLORS[i % len(LABEL_COLORS)]

        parts.append(
            f'<text x="{PAD}" y="{y}" font-family="Consolas,Monaco,monospace" '
            f'font-size="13" fill="{lcolor}"{anim_cls}>{label}:</text>'
        )
        parts.append(
            f'<text x="{PAD + 80}" y="{y}" font-family="Consolas,Monaco,monospace" '
            f'font-size="13" fill="{TEXT_COLOR}"{anim_cls}>{value}</text>'
        )

    parts.append("</svg>")

    out = Path("info-card.svg")
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"Done → {out}")


if __name__ == "__main__":
    main()
