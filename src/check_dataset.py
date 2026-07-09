import os

dataset_path = "dataset/train"

print("Checking Dataset...\n")

classes = os.listdir(dataset_path)

print("Number of Classes:", len(classes))

for folder in classes:
    folder_path = os.path.join(dataset_path, folder)

    if os.path.isdir(folder_path):
        images = os.listdir(folder_path)
        print(f"{folder}: {len(images)} images")