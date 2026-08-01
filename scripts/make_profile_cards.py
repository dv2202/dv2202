#!/usr/bin/env python3
"""Generate static SVG cards for the README hero section."""

from pathlib import Path


BG = "#0d1117"
BG2 = "#111827"
FRAME = "#30363d"
MUTED = "#8b949e"
TEXT = "#c9d1d9"
BLUE = "#58a6ff"
GREEN = "#3fb950"
PURPLE = "#bc8cff"
ORANGE = "#f0883e"


def shell_card(width, height, title, prompt, lines, accent):
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        '<defs>'
        f'<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/>'
        '</linearGradient>'
        '</defs>',
        f'<rect width="{width}" height="{height}" rx="14" fill="url(#bg)"/>',
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="14" fill="none" stroke="{FRAME}"/>',
        f'<line x1="0" y1="34" x2="{width}" y2="34" stroke="{FRAME}"/>',
    ]
    for i, color in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        parts.append(f'<circle cx="{22 + i * 16}" cy="17" r="5" fill="{color}"/>')
    parts.append(f'<text x="{width / 2}" y="22" font-size="12" fill="{MUTED}" text-anchor="middle">{title}</text>')
    parts.append(f'<text x="22" y="62" font-size="13" fill="{GREEN}">$</text>')
    parts.append(f'<text x="42" y="62" font-size="13" fill="{TEXT}">{prompt}</text>')

    y = 94
    for i, line in enumerate(lines):
        label, value, color = line
        parts.append(f'<text x="22" y="{y}" font-size="13" fill="{color}">{label}</text>')
        parts.append(f'<text x="132" y="{y}" font-size="13" fill="{TEXT}">{value}</text>')
        y += 28

    parts.append(f'<rect x="22" y="{height - 38}" width="{width - 44}" height="1" fill="{FRAME}"/>')
    parts.append(f'<text x="22" y="{height - 16}" font-size="12" fill="{accent}">●</text>')
    parts.append(f'<text x="42" y="{height - 16}" font-size="12" fill="{MUTED}">available for building useful software, AI systems</text>')
    parts.append('</svg>')
    return ''.join(parts)


def stack_card(width, height):
    groups = [
        ("languages", "TypeScript, JavaScript, Python, C++", BLUE),
        ("frontend", "React, Next.js, Remix, Tailwind", "#61dafb"),
        ("state", "Redux, Zustand, Jotai, React Query", PURPLE),
        ("backend", "Node.js, Express, REST, GraphQL", GREEN),
        ("realtime", "WebSockets, voice/chat automation", ORANGE),
        ("ai", "LLMs, RAG, AI Agents, Mastra", PURPLE),
        ("data", "MongoDB, Postgres, MySQL, Supabase", BLUE),
        ("platform", "AWS, Docker, Vercel, Git", ORANGE),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        f'<rect width="{width}" height="{height}" rx="14" fill="{BG}"/>',
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="14" fill="none" stroke="{FRAME}"/>',
        f'<text x="22" y="34" font-size="16" font-weight="700" fill="{TEXT}">stack --compact</text>',
        f'<text x="22" y="58" font-size="12" fill="{MUTED}">tools I reach for when shipping</text>',
    ]

    y = 94
    for label, value, color in groups:
        parts.append(f'<rect x="22" y="{y - 18}" width="386" height="24" rx="7" fill="{color}" fill-opacity="0.08"/>')
        parts.append(f'<text x="34" y="{y}" font-size="12" fill="{color}">{label}</text>')
        parts.append(f'<text x="128" y="{y}" font-size="12" fill="{TEXT}">{value}</text>')
        y += 31

    y = height - 58

    parts.append('</svg>')
    return ''.join(parts)


def main():
    about = shell_card(
        430,
        345,
        "devansh@github: ~/about",
        "./about.sh",
        [
            ("name", "Devansh Vishwakarma", BLUE),
            ("role", "Full-Stack AI Engineer @ Forest AI", GREEN),
            ("building", "LLM systems, RAG, agent workflows", PURPLE),
            ("frontend", "React, Next.js, Remix, TypeScript", ORANGE),
            ("backend", "Node.js, APIs, GraphQL, WebSockets", BLUE)
        ],
        GREEN,
    )
    Path("about-card.svg").write_text(about, encoding="utf-8")
    Path("stack-card.svg").write_text(stack_card(430, 345), encoding="utf-8")
    print("wrote about-card.svg and stack-card.svg")


if __name__ == "__main__":
    main()
