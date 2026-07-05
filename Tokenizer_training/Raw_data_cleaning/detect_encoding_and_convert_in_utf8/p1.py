# Method 1 — Try UTF-8 Only

# Ye simplest method hai.

import os

INPUT_FOLDER = "raw_documents"

valid_files = []
invalid_files = []

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            f.read()

        valid_files.append(filename)

    except UnicodeDecodeError:
        invalid_files.append(filename)

print("UTF-8 Files")
print(valid_files)

print()

print("Encoding Failed")
print(invalid_files)


# is code me sirf detect kar rhe hai  dusre encoding me convert nhi kar rhe