"""Rebuild the lightweight skill catalog and browsable Markdown index."""
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/code-animation-prompts"
LIBRARY = SKILL / "assets/library"


def main():
    html = (LIBRARY / "风格挑选.html").read_text(encoding="utf-8")
    raw = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.S).group(1))
    entries = []
    for e in raw["entries"]:
        for field in ["file", "img"]:
            if e.get(field):
                path = (LIBRARY / e[field]).resolve()
                if LIBRARY.resolve() not in path.parents or not path.is_file():
                    raise ValueError(f"Missing or invalid asset: {e[field]}")
        entries.append(dict(id=e["id"], name=e["name"], series=e["s"], category=e["cat"],
                            description=e.get("desc", ""), fit=e.get("fit", ""), tags=e.get("tags", []),
                            file="assets/library/" + e["file"],
                            image="assets/library/" + e["img"] if e.get("img") else ""))
    counts = dict(Counter(e["series"] for e in entries))
    stats = json.loads((LIBRARY / "_统计.json").read_text(encoding="utf-8"))
    assert len(entries) == stats["total"] == len({e["id"] for e in entries})
    assert sum(bool(e["image"]) for e in entries) == stats["withStill"]
    assert counts == stats["bySeries"]
    catalog = dict(total=len(entries), with_still=stats["withStill"],
                   series=[dict(id=m["id"], name=m["label"], count=counts[m["id"]]) for m in raw["meta"]], entries=entries)
    (SKILL / "references/catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# 341 种风格索引", "", "从原始离线挑选器生成。点击名称阅读提示词；196 个条目附静帧，其余为文字参考。", "", "[返回 README](../README.md)", ""]
    for series in catalog["series"]:
        lines += [f'## {series["name"]} · {series["count"]}', "", "| 编号 | 风格 | 参考 |", "|---|---|---|"]
        for e in entries:
            if e["series"] == series["id"]:
                link = "../skills/code-animation-prompts/"
                name = e["name"].replace("|", "\\|")
                shot = f'[静帧]({quote(link + e["image"])})' if e["image"] else "文字参考"
                lines.append(f'| {e["id"]} | [{name}]({quote(link + e["file"])}) | {shot} |')
        lines.append("")
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs/STYLES.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Validated {len(entries)} styles and {stats['withStill']} stills.")


if __name__ == "__main__":
    main()
