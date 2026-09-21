from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / "site" / "styles.css").read_text()
inline = f"<style>\n{css}\n</style>"

for name in ("index.html", "kit-preview.html"):
    path = ROOT / "site" / name
    text = path.read_text()
    marker = '<link rel="stylesheet" href="styles.css">'
    if marker in text:
        updated = text.replace(marker, inline, 1)
    else:
        updated, count = re.subn(r"<style>\n.*?\n</style>", inline, text, count=1, flags=re.S)
        if count != 1:
            raise SystemExit(f"stylesheet block missing in {path}")
    path.write_text(updated)
    print(f"inlined styles into {path}")
