import os
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FOLDER = os.path.join(BASE_DIR, "raw_documents")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ----------------------------
# 1. Valid ZIP File
# ----------------------------
zip_path = os.path.join(OUTPUT_FOLDER, "archive.zip")

with zipfile.ZipFile(zip_path, "w") as z:
    z.writestr("readme.txt", "This is a sample ZIP archive.")
    z.writestr("data.txt", "Hello World!")

# ----------------------------
# 2. Random EXE (Binary)
# ----------------------------
with open(os.path.join(OUTPUT_FOLDER, "program.exe"), "wb") as f:
    f.write(os.urandom(4096))

# ----------------------------
# 3. Random MP3 (Binary)
# ----------------------------
with open(os.path.join(OUTPUT_FOLDER, "song.mp3"), "wb") as f:
    f.write(os.urandom(8192))

# ----------------------------
# 4. Random MP4 (Binary)
# ----------------------------
with open(os.path.join(OUTPUT_FOLDER, "vedio_song.mp4"), "wb") as f:
    f.write(os.urandom(16384))

# ----------------------------
# 5. Valid JPEG
# ----------------------------
jpeg_path = os.path.join(OUTPUT_FOLDER, "image.jpeg")

jpeg_header = bytes([
    0xFF, 0xD8,       # SOI
    0xFF, 0xE0,
    0x00, 0x10,
    0x4A, 0x46, 0x49, 0x46,
    0x00, 0x01,
    0x01, 0x01,
    0x00, 0x60,
    0x00, 0x60,
    0x00, 0x00
])

jpeg_footer = bytes([0xFF, 0xD9])

with open(jpeg_path, "wb") as f:
    f.write(jpeg_header)
    f.write(os.urandom(5000))
    f.write(jpeg_footer)


with open(os.path.join(OUTPUT_FOLDER, "binary_file.txt"), "wb") as f:
    f.write(os.urandom(4096)) 

print("Sample binary files created successfully!")


#binary files  bnane ke liye