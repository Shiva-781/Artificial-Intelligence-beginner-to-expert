# Method 6 — Folder ki Sabhi Files Normalize Karna
# Code
import os
import re

INPUT_FOLDER = "raw_documents"
OUTPUT_FOLDER = "clean_documents"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Multiple spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Multiple blank lines
    text = re.sub(r"\n{2,}", "\n\n", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    output_path = os.path.join(OUTPUT_FOLDER, filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"{filename} normalized")