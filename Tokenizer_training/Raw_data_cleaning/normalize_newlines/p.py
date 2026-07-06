import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FOLDER = os.path.join(BASE_DIR, "raw_documents")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

lines = [
    "Hello World",
    "How are you?",
    "Python",
    "Tokenizer Training",
    "OpenAI"
]

# 1. Windows (CRLF)
with open(os.path.join(OUTPUT_FOLDER, "windows_crlf.txt"), "wb") as f:
    f.write("\r\n".join(lines).encode("utf-8"))

# 2. Linux (LF)
with open(os.path.join(OUTPUT_FOLDER, "linux_lf.txt"), "wb") as f:
    f.write("\n".join(lines).encode("utf-8"))

# 3. Old Mac (CR)
with open(os.path.join(OUTPUT_FOLDER, "mac_cr.txt"), "wb") as f:
    f.write("\r".join(lines).encode("utf-8"))

# 4. Mixed Line Endings
mixed = (
    "Hello World\r\n"
    "How are you?\n"
    "Python\r"
    "Tokenizer\r\n"
    "OpenAI\n"
)

with open(os.path.join(OUTPUT_FOLDER, "mixed_newlines.txt"), "wb") as f:
    f.write(mixed.encode("utf-8"))

# 5. No Newline at EOF
no_newline = "Hello World\nHow are you?\nPython"

with open(os.path.join(OUTPUT_FOLDER, "no_newline_eof.txt"), "wb") as f:
    f.write(no_newline.encode("utf-8"))

# 6. Empty File
open(os.path.join(OUTPUT_FOLDER, "empty.txt"), "wb").close()

# 7. One Line
with open(os.path.join(OUTPUT_FOLDER, "single_line.txt"), "wb") as f:
    f.write(b"Only one line")

# 8. Blank Lines
blank = "Hello\n\n\nPython\n\nOpenAI\n"

with open(os.path.join(OUTPUT_FOLDER, "blank_lines.txt"), "wb") as f:
    f.write(blank.encode("utf-8"))

# 9. Leading & Trailing Spaces
spaces = "   Hello World   \n\tPython\t\n   OpenAI"

with open(os.path.join(OUTPUT_FOLDER, "spaces_tabs.txt"), "wb") as f:
    f.write(spaces.encode("utf-8"))

# 10. Unicode Text
unicode_text = (
    "नमस्ते दुनिया\n"
    "こんにちは世界\n"
    "你好，世界\n"
    "안녕하세요\n"
    "😀 😎 🚀\n"
)

with open(os.path.join(OUTPUT_FOLDER, "unicode.txt"), "wb") as f:
    f.write(unicode_text.encode("utf-8"))

print("All newline test files created successfully.")


# run karne Par 

# Ye files banengi
# raw_documents/
# │
# ├── windows_crlf.txt        (Windows CRLF)
# ├── linux_lf.txt            (Linux LF)
# ├── mac_cr.txt              (Old Mac CR)
# ├── mixed_newlines.txt      (CRLF + LF + CR mixed)
# ├── no_newline_eof.txt      (EOF without newline)
# ├── empty.txt               (0 bytes)
# ├── single_line.txt         (Single line)
# ├── blank_lines.txt         (Multiple blank lines)
# ├── spaces_tabs.txt         (Spaces + Tabs)
# └── unicode.txt             (Unicode text)