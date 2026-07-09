import os

print("Current Working Directory:")
print(os.getcwd())

print("\nChecking if dataset exists:")
print(os.path.exists("dataset"))

print("\nChecking if train exists:")
print(os.path.exists("dataset/train"))

print("\nContents of dataset:")

if os.path.exists("dataset"):
    print(os.listdir("dataset"))