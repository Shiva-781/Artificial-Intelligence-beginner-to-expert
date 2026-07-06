# Method 4 — MD5 Hash
import os
import hashlib

INPUT_FOLDER = "raw_documents"

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



    
# Expected Output
# ======================================================================
# Filename                       MD5 Hash
# ======================================================================
# article1.txt                   7b2e2b...
# article1_copy.txt              7b2e2b...   ← Same
# article1_modified.txt          a81f92...
# article2.txt                   2bc7d1...
# article2_duplicate.txt         2bc7d1...   ← Same
# article2_modified.txt          f1b48e...
# article3.txt                   c2a71d...
# empty1.txt                     d41d8cd98f00b204e9800998ecf8427e
# empty2.txt                     d41d8cd98f00b204e9800998ecf8427e   ← Same
# binary1.bin                    91e5c3...
# binary1_copy.bin               91e5c3...   ← Same
# binary2.bin                    3fa9b7...
