# Method 3 — Compare Text Instead of Bytes

# Agar encoding already UTF-8 hai

import os

INPUT_FOLDER = "raw_documents"

seen = set()

for filename in os.listdir(INPUT_FOLDER):

    path = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(path):
        continue

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    if text in seen:

        print("Duplicate:", filename)

    else:

        seen.add(text)


# Ye small datasets ke liye theek hai.

# Large corpus ke liye hashing use karna chahiye.