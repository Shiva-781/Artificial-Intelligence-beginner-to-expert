#method3
import os

INPUT_FOLDER = "raw_documents"

binary_files = []
text_files = []

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    try:
        # Binary mode me first 4096 bytes read karo
        with open(filepath, "rb") as f:
            chunk = f.read(4096)

        # Null byte mila?
        if b"\x00" in chunk:
            binary_files.append(filename)
            continue

        # UTF-8 decode test
        chunk.decode("utf-8")

        text_files.append(filename)

    except UnicodeDecodeError:
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