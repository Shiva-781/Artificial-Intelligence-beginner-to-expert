import os

# User se folder path lo
INPUT_FOLDER = input("Enter input folder path: ").strip()

# Check if folder exists
if not os.path.isdir(INPUT_FOLDER):
    print("Folder does not exist!")
    exit()

# Valid files ki list
valid_files = []

# Corrupted files ki list
corrupted_files = []

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    # Sirf files process karo
    if not os.path.isfile(filepath):
        continue

    try:
        # UTF-8 me read karne ki koshish
        with open(filepath, "r", encoding="utf-8") as f:
            f.read()

        valid_files.append(filename)

    except Exception:
        corrupted_files.append(filename)

print("=" * 40)
print("VALID FILES")
print("=" * 40)

for file in valid_files:
    print(file)

print("\n")

print("=" * 40)
print("CORRUPTED FILES")
print("=" * 40)

for file in corrupted_files:
    print(file)