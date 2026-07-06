# Method 1 — Exact Duplicate using SHA-256 (Industry Standard)

# Sabse pehle document ka hash nikala jata hai.

# Same document ⇒ Same hash

# Different document ⇒ Different hash

# Complete Code
import os
import hashlib

INPUT_FOLDER = "raw_documents"

seen_hashes = set()

unique_files = []
duplicate_files = []

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    with open(filepath, "rb") as f:
        data = f.read()

    file_hash = hashlib.sha256(data).hexdigest()

    if file_hash in seen_hashes:
        duplicate_files.append(filename)
    else:
        seen_hashes.add(file_hash)
        unique_files.append(filename)

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