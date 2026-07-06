# Method 5 — Duplicate After Normalization

# Kabhi documents me sirf extra spaces ka difference hota hai.




import os
import hashlib
import re

INPUT_FOLDER = "raw_documents"

seen_hashes = set()

unique_files = []
duplicate_files = []

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    try:
        # Text file read
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        # ----------------------------
        # Normalize Text
        # ----------------------------

        # Remove leading/trailing spaces
        text = text.strip()

        # Convert all whitespace (spaces, tabs, newlines) to single space
        text = re.sub(r"\s+", " ", text)

        # ----------------------------
        # SHA-256 Hash
        # ----------------------------

        file_hash = hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

        if file_hash in seen_hashes:
            duplicate_files.append(filename)
        else:
            seen_hashes.add(file_hash)
            unique_files.append(filename)

    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("=" * 40)
print("UNIQUE FILES")
print("=" * 40)

for file in unique_files:
    print(file)

print()

print("=" * 40)
print("DUPLICATE FILES")
print("=" * 40)

for file in duplicate_files:
    print(file)

# Ab dono ka hash same ban jayega.