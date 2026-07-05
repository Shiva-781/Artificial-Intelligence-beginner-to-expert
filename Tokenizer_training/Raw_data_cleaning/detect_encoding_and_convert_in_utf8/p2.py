# Method 2 — Detect Encoding Automatically (Recommended)

# Install library

# pip install charset-normalizer

import os
from charset_normalizer import from_bytes

INPUT_FOLDER = "raw_documents"

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    with open(filepath, "rb") as f:
        raw_data = f.read()

    result = from_bytes(raw_data).best()

    if result is None:
        print(f"{filename} -> Encoding Not Detected")
        continue

    print(f"{filename}")

    print("Detected Encoding :", result.encoding)

    print("Language :", result.language)

    print("-" * 40)



# is code me sirf detect kar rhe hai  dusre encoding me convert nhi kar rhe