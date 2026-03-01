import json, os

CATS = {
  "Nature": "assets/gallery/nature",
  "Travel": "assets/gallery/travel",
  "Victory Garden Initiative": "assets/gallery/vgi",
  "Drone shots": "assets/gallery/drone",
  "Skyline": "assets/gallery/skyline",
  "Dogs": "assets/gallery/dogs",
}

EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".heic"}

def list_images(folder):
  if not os.path.isdir(folder):
    return []
  files = []
  for name in sorted(os.listdir(folder)):
    if name.startswith("."):
      continue
    ext = os.path.splitext(name)[1].lower()
    if ext in EXTS:
      files.append("/" + folder + "/" + name)
  return files

out = {cat: list_images(path) for cat, path in CATS.items()}

os.makedirs("assets/gallery", exist_ok=True)
with open("assets/gallery/photos.json", "w") as f:
  json.dump(out, f, indent=2)

print("✅ Wrote assets/gallery/photos.json")
for k, v in out.items():
  print(f"{k}: {len(v)} files")