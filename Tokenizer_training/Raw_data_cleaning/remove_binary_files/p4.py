import os
import string

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FOLDER = os.path.join(BASE_DIR, "raw_documents")

binary_files = []
text_files = []

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    try:
        with open(filepath, "rb") as f:
            chunk = f.read(4096)

        # Empty file
        if len(chunk) == 0:
            text_files.append(filename)
            continue

        # Null byte => Binary
        if b"\x00" in chunk:
            binary_files.append(filename)
            continue

        # UTF-8 Decode
        try:
            text = chunk.decode("utf-8")
        except UnicodeDecodeError:
            binary_files.append(filename)
            continue

        # Printable Character Ratio
        printable = sum(c in string.printable for c in text)

        ratio = printable / len(text)

        if ratio > 0.95:
            text_files.append(filename)
        else:
            binary_files.append(filename)

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