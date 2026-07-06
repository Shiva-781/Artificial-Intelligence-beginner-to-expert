# Method 2 — Using Regular Expression

# Useful jab mixed newline characters ho.

# Complete Code
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

    # Replace every newline style with \n
    text = re.sub(r"\r\n|\r", "\n", text)

    output_path = os.path.join(OUTPUT_FOLDER, filename)

    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    print(f"{filename} normalized")