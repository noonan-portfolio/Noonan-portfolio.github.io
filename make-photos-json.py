import json, os

# Top-level categories you want as tabs
CATS = {
  "Nature": ["assets/gallery/nature", "assets/gallery/Nature"],
  "Travel": ["assets/gallery/travel", "assets/gallery/travel-trips", "assets/gallery/Travel"],
  "Skyline": ["assets/gallery/skyline", "assets/gallery/Skyline"],
  "Victory Garden Initiative": ["assets/gallery/vgi", "assets/gallery/VGI"],
}

EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".heic"}  # ext check uses .lower()

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
    full = os.path.join(folder, name)
    if not os.path.isfile(full):
      continue
    ext = os.path.splitext(name)[1].lower()
    if ext in EXTS:
      files.append("/" + folder + "/" + name)
  return files

def travel_subcats(travel_root):
  """
  Travel subcategories (folders) -> display names.
  Add/adjust mappings here as needed.
  """
  return {
    "iceland-2018": "Iceland 2018",
    "yearly-river-trips-bwca": "Yearly River Trips / BWCA",
  }

out = {}

for cat, options in CATS.items():
  folder = first_existing(options)

  if cat == "Travel":
    travel_obj = {}
    root = folder
    mapping = travel_subcats(root)

    # Ensure keys exist even if folders are missing/empty
    for slug, display in mapping.items():
      travel_obj[display] = []

    if root and os.path.isdir(root):
      for slug, display in mapping.items():
        subdir = os.path.join(root, slug)
        travel_obj[display] = list_images(subdir)

    out["Travel"] = travel_obj
  else:
    out[cat] = list_images(folder)

os.makedirs("assets/gallery", exist_ok=True)
with open("assets/gallery/photos.json", "w") as f:
  json.dump(out, f, indent=2)

print("✅ Wrote assets/gallery/photos.json")
for k, v in out.items():
  if k == "Travel" and isinstance(v, dict):
    print("Travel:")
    for sk, sv in v.items():
      print(f"  {sk}: {len(sv)} files")
  else:
    print(f"{k}: {len(v)} files")
