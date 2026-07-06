# Method 1 — Remove Fixed Boilerplate (Simple)

# Agar tumhe pata hai kaunsi lines remove karni hain.

# Code
import os

INPUT_FOLDER = "raw_documents"
OUTPUT_FOLDER = "clean_documents"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

BOILERPLATE = [
    "Privacy Policy",
    "Terms of Service",
    "Cookie Policy",
    "Home",
    "About",
    "Contact",
    "Subscribe",
    "Login"
]

for filename in os.listdir(INPUT_FOLDER):

    filepath = os.path.join(INPUT_FOLDER, filename)

    if not os.path.isfile(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned = []

    for line in lines:

        if line.strip() not in BOILERPLATE:
            cleaned.append(line)

    output = os.path.join(OUTPUT_FOLDER, filename)

    with open(output, "w", encoding="utf-8") as f:
        f.writelines(cleaned)

print("Done")