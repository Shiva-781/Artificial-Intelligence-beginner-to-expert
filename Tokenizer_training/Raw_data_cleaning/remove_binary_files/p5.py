import os
from binaryornot.check import is_binary

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FOLDER = os.path.join(BASE_DIR, "raw_documents")

binary_files = []
text_files = []

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    try:
        if is_binary(filepath):
            binary_files.append(filename)
        else:
            text_files.append(filename)

    except Exception as e:
        print(f"Error reading {filename}: {e}")

print("=" * 40)
print("TEXT FILES")
print("=" * 40)

for file in text_files:
    print(file)

print()

print("=" * 40)
print("BINARY FILES")
print("=" * 40)

for file in binary_files:
    print(file)