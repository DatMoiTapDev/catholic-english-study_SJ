from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(__file__).resolve().parents[1]
dist = root / "dist"
archive = root / "assets.zip"
if archive.exists():
    with ZipFile(archive) as resources:
        resources.extractall(root)
for n in range(1, 27):
    folder = dist / "units" / f"Unit{n}"
    with ZipFile(folder / f"Unit{n}_Bo_3_file.zip", "w", ZIP_DEFLATED) as z:
        for f in sorted(folder.iterdir()):
            if f.suffix in (".pdf", ".docx"): z.write(f, f.name)
with ZipFile(dist / "Units_02_26_Theo_Mau_Unit1.zip", "w", ZIP_DEFLATED) as z:
    for n in range(2, 27):
        for f in sorted((dist / "units" / f"Unit{n}").iterdir()):
            if f.suffix in (".pdf", ".docx"): z.write(f, f.relative_to(dist / "units"))
        z.write(dist / "audio" / f"{n:02}.mp3", f"audio/{n:02}.mp3")
with ZipFile(dist / "Catholic_English_Complete.zip", "w", ZIP_DEFLATED) as z:
    for f in sorted(root.rglob("*")):
        if not f.is_file() or any(p.startswith(".") or p == "__pycache__" for p in f.relative_to(root).parts): continue
        if f.name in ("Catholic_English_Complete.zip", "assets.zip"): continue
        z.write(f, f.relative_to(root))
print("Download ZIPs are ready.")
