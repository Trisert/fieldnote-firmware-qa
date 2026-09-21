from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "kit"
DIST = ROOT / "dist"
OUTPUT = DIST / "embedded-firmware-qa-starter-kit-v0.1.0.zip"


def build() -> None:
    DIST.mkdir(exist_ok=True)
    if OUTPUT.exists():
        OUTPUT.unlink()
    files = sorted(path for path in KIT.rglob("*") if path.is_file())
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, Path("embedded-firmware-qa-starter-kit") / path.relative_to(KIT))
    print(f"built {OUTPUT} ({len(files)} files)")


if __name__ == "__main__":
    build()
