import os
import cv2
import numpy as np

# ==============================
# Dataset Path
# ==============================
dataset_path = os.path.join("dataset", "train")

# Emotion Labels
emotion_labels = {
    "Angry": 0,
    "Disgust": 1,
    "Fear": 2,
    "Happy": 3,
    "Neutral": 4,
    "Sad": 5,
    "Surprise": 6
}

images = []
labels = []

print("=" * 50)
print("Loading Dataset...")
print("=" * 50)

# Check dataset exists
if not os.path.exists(dataset_path):
    print("Dataset folder not found!")
    print("Expected:", dataset_path)
    exit()

# Loop through each emotion folder
for emotion in emotion_labels.keys():

    folder_path = os.path.join(dataset_path, emotion)

    print("\nChecking:", folder_path)

    if not os.path.exists(folder_path):
        print("Folder not found:", folder_path)
        continue

    image_files = os.listdir(folder_path)

    print(f"Found {len(image_files)} images.")

    for file in image_files:

        image_path = os.path.join(folder_path, file)

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            print("Skipped:", image_path)
            continue

        image = cv2.resize(image, (48, 48))

        images.append(image)

        labels.append(emotion_labels[emotion])

# Convert to NumPy arrays
images = np.array(images)
labels = np.array(labels)

print("\n" + "=" * 50)
print("Dataset Loaded Successfully!")
print("=" * 50)

print("Images Shape :", images.shape)
print("Labels Shape :", labels.shape)

print("\nLabel Distribution")

for emotion, label in emotion_labels.items():
    count = np.sum(labels == label)
    print(f"{emotion}: {count}")

print("\nDone!")