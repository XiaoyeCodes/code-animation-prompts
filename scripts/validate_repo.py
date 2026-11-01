"""Validate original asset hashes, catalog references and authored documentation links."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/code-animation-prompts"
LIBRARY = SKILL / "assets/library"


def main():
    manifest = json.loads((ROOT / "docs/source-manifest.json").read_text(encoding="utf-8"))
    files = {p.relative_to(LIBRARY).as_posix(): p for p in LIBRARY.rglob("*") if p.is_file()}
    assert set(files) == set(manifest["files"]), "Original library file set differs"
    for name, digest in manifest["files"].items():
        assert hashlib.sha256(files[name].read_bytes()).hexdigest() == digest, f"Original file changed: {name}"
    data = json.loads((SKILL / "references/catalog.json").read_text(encoding="utf-8"))
    assert data["total"] == len(data["entries"]) == 341
    assert len({e["id"] for e in data["entries"]}) == 341
    assert sum(bool(e["image"]) for e in data["entries"]) == data["with_still"] == 196
    for entry in data["entries"]:
        for key in ["file", "image"]:
            if entry[key]:
                assert (SKILL / entry[key]).is_file(), entry[key]
    checked = 0
    for doc in ROOT.rglob("*.md"):
        if any(part in {".git", ".build", ".agents", ".claude"} for part in doc.relative_to(ROOT).parts):
            continue
        if LIBRARY in doc.parents:
            continue  # Original documents are retained verbatim.
        for target in re.findall(r'\]\(([^)]+)\)', doc.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:", "mailto:", "#")):
                continue
            path = unquote(target.split("#")[0])
            assert (doc.parent / path).exists(), f"Broken link: {doc.relative_to(ROOT)} -> {target}"
            checked += 1
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    prompt = re.search(r'```text\n(请将 https://github.com/XiaoyeCodes/code-animation-prompts.*?)(?:\n```)', readme, re.S).group(1)
    assert prompt in (ROOT / "prompts/one-click-import.md").read_text(encoding="utf-8")
    print(f"PASS: {len(files)} original files unchanged; 341 styles; 196 stills; {checked} local links; import prompt consistent.")


if __name__ == "__main__":
    main()
