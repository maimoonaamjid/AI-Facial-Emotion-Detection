import os

for root, dirs, files in os.walk("dataset"):
    print(root)