from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / "site" / "styles.css").read_text()
marker = '<link rel="stylesheet" href="styles.css">'
inline = f"<style>\n{css}\n</style>"

for name in ("index.html", "kit-preview.html"):
    path = ROOT / "site" / name
    text = path.read_text()
    if marker not in text:
        raise SystemExit(f"stylesheet marker missing in {path}")
    path.write_text(text.replace(marker, inline, 1))
    print(f"inlined styles into {path}")
