import os
import cv2
import matplotlib.pyplot as plt

# Path to dataset
dataset_path = "dataset/train"

# Emotion classes
classes = os.listdir(dataset_path)

print("Available Classes:")
print(classes)

# Display one image from each class
plt.figure(figsize=(12, 8))

for i, emotion in enumerate(classes):

    emotion_path = os.path.join(dataset_path, emotion)

    image_name = os.listdir(emotion_path)[0]

    image_path = os.path.join(emotion_path, image_name)

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    plt.subplot(2, 4, i + 1)
    plt.imshow(image, cmap='gray')
    plt.title(emotion)
    plt.axis("off")

plt.tight_layout()
plt.show()