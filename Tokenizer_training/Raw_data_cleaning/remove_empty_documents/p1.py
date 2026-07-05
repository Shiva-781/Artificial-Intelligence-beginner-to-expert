import os

# Raw documents folder
INPUT_FOLDER = "raw_documents"

# Lists
empty_files = []
non_empty_files = []

# Process every file
for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    # Ignore folders
    if not os.path.isfile(filepath):
        continue

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        # Remove leading/trailing whitespace
        if len(text.strip()) == 0:
            empty_files.append(filename)
        else:
            non_empty_files.append(filename)

    except Exception as e:
        print(f"Cannot read {filename}: {e}")

print("=" * 40)
print("NON EMPTY FILES")
print("=" * 40)

for file in non_empty_files:
    print(file)

print()

print("=" * 40)
print("EMPTY FILES")
print("=" * 40)

for file in empty_files:
    print(file)