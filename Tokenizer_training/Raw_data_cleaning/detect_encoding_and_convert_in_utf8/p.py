import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FOLDER = os.path.join(BASE_DIR, "raw_documents")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

text = """
Hello World!
My name is ChatGPT.
This file is created for encoding testing.

English Text
1234567890

Encoding Test:
UTF-8
UTF-16
UTF-32
ASCII
Latin-1
Windows-1252

Café
Résumé
naïve
España
"""

files = [
    ("utf8.txt", "utf-8"),
    ("utf16.txt", "utf-16"),
    ("utf32.txt", "utf-32"),
    ("ascii.txt", "ascii"),
    ("latin1.txt", "latin-1"),
    ("windows1252.txt", "cp1252"),
]

for filename, encoding in files:

    filepath = os.path.join(OUTPUT_FOLDER, filename)

    try:
        with open(filepath, "w", encoding=encoding) as f:
            f.write(text)

        print(f"Created: {filename} ({encoding})")

    except UnicodeEncodeError:
        # ASCII me unsupported characters hata do
        with open(filepath, "w", encoding=encoding, errors="replace") as f:
            f.write(text)

        print(f"Created: {filename} ({encoding}) [unsupported chars replaced]")

print("\nAll encoding files created successfully.")

#ye  sirf  alag alag type ke encoding content bali file banane ke liye