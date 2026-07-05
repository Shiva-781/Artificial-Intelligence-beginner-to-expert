#method1

import os

INPUT_FOLDER = "raw_documents"

# Common binary extensions
BINARY_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".webp",
    ".pdf",
    ".zip",
    ".rar",
    ".7z",
    ".tar",
    ".gz",
    ".exe",
    ".dll",
    ".so",
    ".bin",
    ".iso",
    ".mp3",
    ".wav",
    ".mp4",
    ".avi",
    ".mov",
    ".mkv"
}

binary_files = []
text_files = []

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    extension = os.path.splitext(filename)[1].lower()

    if extension in BINARY_EXTENSIONS:
        binary_files.append(filename)
    else:
        text_files.append(filename)

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



#isme  ek dikkat hai ho sakta hai binary extension ho aur data txt 
#ya binary extension na ho aur data binry ho file me   to galat detection ho jayegi  isliye ye method avoid kare
#  jaise   binary_file.txt me data binary hai   jo ki p2.py ya p3.py ke output se samjh aa jayega