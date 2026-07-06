# Method 3 — Normalize Every .txt File in Folder
import os

folder = "raw_documents"

for filename in os.listdir(folder):

    path = os.path.join(folder, filename)

    if not os.path.isfile(path):
        continue

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

print("All files normalized.")

# Ye original files ko overwrite karega.