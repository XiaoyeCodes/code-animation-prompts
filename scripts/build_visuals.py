"""Render README artwork from the real bundled stills and picker with Playwright."""
import html
import json
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/code-animation-prompts"
OUT = ROOT / "docs/images"
BUILD = ROOT / ".build"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(exist_ok=True)
    entries = json.loads((SKILL / "references/catalog.json").read_text(encoding="utf-8"))["entries"]
    by_id = {e["id"]: e for e in entries}

    def card(id):
        e = by_id[id]
        src = (SKILL / e["image"]).as_uri()
        return f'<article><img src="{src}"><div><b>{id}</b><span>{html.escape(e["name"])}</span></div></article>'

    css = '''*{box-sizing:border-box}body{margin:0;font-family:"Segoe UI","Microsoft YaHei",sans-serif;background:#0d111a;color:#f4f6fa} .topline{font-size:14px;letter-spacing:3px;color:#b7f47b}h1,h2,p{margin:0}article{overflow:hidden;border:1px solid #29313e;border-radius:14px;background:#141c28}article img{width:100%;aspect-ratio:16/9;object-fit:contain;display:block;background:#0a0c13}article div{display:flex;align-items:center;gap:14px;padding:16px 18px}article b{color:#b7f47b;font-family:Consolas,monospace;font-size:15px}article span{color:#dce2ed;font-size:16px}.muted{color:#8b96aa}.foot{font-size:13px;letter-spacing:1px;color:#8591a6;display:flex;justify-content:space-between}'''
    hero = f'''<!doctype html><meta charset="utf-8"><style>{css}
    body{{padding:56px 64px;width:1600px;height:660px;background:radial-gradient(ellipse at 82% 18%,#233529,transparent 55%),#0d111a}}
    main{{display:grid;grid-template-columns:1.02fr 1fr;gap:64px;align-items:center;height:518px}}
    h1{{font-size:76px;line-height:1.02;letter-spacing:-3px;margin:27px 0 22px}}h1 em{{font-style:normal;color:#b7f47b}}h2{{font-size:27px;font-weight:500;margin-bottom:18px}}p{{font-size:18px;color:#9ba7ba;line-height:1.8}}
    .chips{{display:flex;gap:12px;margin-top:30px}}.chips span{{border:1px solid #374739;padding:10px 15px;border-radius:30px;font-size:14px;color:#d8e8ce}}
    .tiles{{display:grid;grid-template-columns:1fr 1fr;gap:15px;transform:rotate(-2deg)}}article div{{padding:12px 14px}}.foot{{margin-top:25px}}
    </style><main><section><div class="topline">THE CODE ANIMATION STYLE LIBRARY</div><h1>Code.<br>Motion.<br><em>341 possibilities.</em></h1><h2>让代码成为你的动画工作室。</h2><p>风格提示词 × 真实参考静帧 × 可安装 Agent Skill</p><div class="chips"><span>Claude Code</span><span>Codex</span><span>Free to share</span></div></section><section class="tiles">{''.join(card(x) for x in ['R1','Z5','B3','R5'])}</section></main><div class="foot"><span>XIAOYECODES / CODE-ANIMATION-PROMPTS</span><span>341 STYLES · 196 STILLS · 10 SERIES</span></div>'''
    gallery = f'''<!doctype html><meta charset="utf-8"><style>{css}body{{width:1600px;padding:52px 56px}}h1{{font-size:40px;margin:14px 0}}p{{color:#94a0b4;font-size:18px;margin-bottom:30px}}.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}}.foot{{margin-top:28px}}</style><div class="topline">A SMALL WINDOW INTO 341 STYLES</div><h1>一种内容，许多种表达。</h1><p>以下为素材包自带的真实参考静帧；每张图都能通过编号找到对应提示词。</p><div class="grid">{''.join(card(x) for x in ['B1','B3','C1','Z5','H1','L1','L10','R1','R3','R5','R6','O91'])}</div><div class="foot"><span>REFERENCE STILLS FROM THE INCLUDED LIBRARY</span><span>196 WITH STILLS / 145 TEXT REFERENCES</span></div>'''
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width":1600,"height":1000}, device_scale_factor=1)
        for name, content in [("hero", hero), ("style-gallery", gallery)]:
            path = BUILD / f"{name}.html"
            path.write_text(content, encoding="utf-8")
            page.goto(path.as_uri())
            page.evaluate("document.fonts.ready")
            page.locator("img").evaluate_all("imgs => Promise.all(imgs.map(i => i.decode()))")
            page.locator("body").screenshot(path=str(OUT / f"{name}.png"))
        page.goto((SKILL / "assets/library/风格挑选.html").as_uri())
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(800)
        page.screenshot(path=str(OUT / "style-picker.png"))
        page.locator('#q').fill('R1')
        page.wait_for_timeout(500)
        page.screenshot(path=str(OUT / "picker-search.png"))
        browser.close()
    subprocess.run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", "3", "-t", "4",
        "-i", str(SKILL / "assets/library/示例/B6_光速穿梭·爆炸·重聚_同一份提示词/Opus5.5_High.mp4"),
        "-filter_complex", "fps=10,scale=640:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=none",
        "-loop", "0", str(OUT / "b6-preview.gif")
    ], check=True)
    print("README visuals rendered from original assets.")


if __name__ == "__main__":
    main()
