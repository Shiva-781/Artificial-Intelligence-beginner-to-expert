# Method 6 — Duplicate Documents ko Output Folder me Copy Karna
import os
import shutil
import hashlib

INPUT_FOLDER = "raw_documents"
OUTPUT_FOLDER = "unique_documents"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

seen = set()

for filename in os.listdir(INPUT_FOLDER):

    path = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(path):
        continue

    with open(path,"rb") as f:
        data = f.read()

    file_hash = hashlib.sha256(data).hexdigest()

    if file_hash not in seen:

        seen.add(file_hash)

        shutil.copy(path, OUTPUT_FOLDER)

print("Unique corpus created.")