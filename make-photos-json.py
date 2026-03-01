import json, os

CATS = {
  "Nature": ["assets/gallery/nature", "assets/gallery/Nature"],
  "Travel": ["assets/gallery/travel", "assets/gallery/travel-trips", "assets/gallery/Travel"],
  "Victory Garden Initiative": ["assets/gallery/vgi", "assets/gallery/VGI"],
  "Drone shots": ["assets/gallery/drone", "assets/gallery/Drone", "assets/gallery/drone-shots"],
  "Skyline": ["assets/gallery/skyline", "assets/gallery/Skyline"],
  "Dogs": ["assets/gallery/dogs", "assets/gallery/Dogs"],
}

EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".heic"}

def first_existing(paths):
  for p in paths:
    if os.path.isdir(p):
      return p
  return None

def list_images(folder):
  if not folder or not os.path.isdir(folder):
    return []
  files = []
  for name in sorted(os.listdir(folder)):
    if name.startswith("."):
      continue
    ext = os.path.splitext(name)[1].lower()
    if ext in EXTS:
      files.append("/" + folder + "/" + name)
  return files

out = {}
for cat, options in CATS.items():
  folder = first_existing(options)
  out[cat] = list_images(folder)

os.makedirs("assets/gallery", exist_ok=True)
with open("assets/gallery/photos.json", "w") as f:
  json.dump(out, f, indent=2)

print("✅ Wrote assets/gallery/photos.json")
for k, v in out.items():
  print(f"{k}: {len(v)} files")
