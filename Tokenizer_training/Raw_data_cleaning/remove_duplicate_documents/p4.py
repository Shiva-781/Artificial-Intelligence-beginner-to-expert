# Method 4 — MD5 Hash

import os
import hashlib

INPUT_FOLDER = "raw_documents"

seen_hashes = {}
duplicates = []

print("=" * 70)
print(f"{'Filename':30} {'MD5 Hash'}")
print("=" * 70)

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    with open(filepath, "rb") as f:
        data = f.read()

    md5_hash = hashlib.md5(data).hexdigest()

    print(f"{filename:30} {md5_hash}")

    if md5_hash in seen_hashes:
        duplicates.append((filename, seen_hashes[md5_hash]))
    else:
        seen_hashes[md5_hash] = filename

print("\n" + "=" * 40)
print("DUPLICATE FILES (MD5)")
print("=" * 40)

for duplicate, original in duplicates:
    print(f"{duplicate}  -->  {original}")





# MD5 faster hai.

# Lekin production NLP me usually

# SHA-256

# prefer kiya jata hai.