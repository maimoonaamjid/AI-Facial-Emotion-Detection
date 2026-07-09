import os
import cv2

folder = os.path.join("dataset", "train", "Disgust")

print("Folder:", folder)
print("Exists:", os.path.exists(folder))
print()

if not os.path.exists(folder):
    print("Folder not found!")
    exit()

files = os.listdir(folder)

print("Total files:", len(files))
print()

for file in files:
    path = os.path.join(folder, file)

    img = cv2.imread(path)

    if img is None:
        print("❌ Cannot read:", file)
    else:
        print("✅ OK:", file)