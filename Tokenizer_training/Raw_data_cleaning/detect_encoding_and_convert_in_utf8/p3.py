# Method 3 — Detect + Convert to UTF-8 (Industry)

# Ye sabse useful method hai.



# Sab UTF-8 me convert ho jayengi.

import os
from charset_normalizer import from_bytes

INPUT_FOLDER = "raw_documents"
OUTPUT_FOLDER = "clean_documents"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    with open(filepath, "rb") as f:
        raw = f.read()

    result = from_bytes(raw).best()

    if result is None:
        print(f"Skipping {filename}")
        continue

    text = str(result)

    output_path = os.path.join(OUTPUT_FOLDER, filename)

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(text)

    print(f"{filename} converted to UTF-8")


# clean_documents   folder aur iske run karne  se bna hai