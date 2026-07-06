# Method 1 — Using replace() (Most Common)
# Complete Code
import os

INPUT_FOLDER = "raw_documents"
OUTPUT_FOLDER = "clean_documents"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Windows -> Linux
    text = text.replace("\r\n", "\n")

    # Old Mac -> Linux
    text = text.replace("\r", "\n")

    output_path = os.path.join(OUTPUT_FOLDER, filename)

    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    print(f"{filename} normalized")