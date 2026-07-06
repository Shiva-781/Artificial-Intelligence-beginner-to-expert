# Method 2 — Delete Duplicate Files
import os
import hashlib

INPUT_FOLDER = "raw_documents"

seen_hashes = set()

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    with open(filepath, "rb") as f:
        data = f.read()

    file_hash = hashlib.sha256(data).hexdigest()

    if file_hash in seen_hashes:

        os.remove(filepath)

        print(f"Deleted Duplicate : {filename}")

    else:

        seen_hashes.add(file_hash)