import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FOLDER = os.path.join(BASE_DIR, "raw_documents")

os.makedirs(INPUT_FOLDER, exist_ok=True)

# -------------------------
# Original Files
# -------------------------

text1 = """Python is an amazing programming language.
It is used for AI, Machine Learning, Data Science.
"""

text2 = """Artificial Intelligence is changing the world.
Machine Learning is a subset of AI.
"""

text3 = """Tokenizer training requires clean datasets.
Duplicate documents should be removed.
"""

with open(os.path.join(INPUT_FOLDER, "article1.txt"), "w", encoding="utf-8") as f:
    f.write(text1)

with open(os.path.join(INPUT_FOLDER, "article2.txt"), "w", encoding="utf-8") as f:
    f.write(text2)

with open(os.path.join(INPUT_FOLDER, "article3.txt"), "w", encoding="utf-8") as f:
    f.write(text3)

# -------------------------
# Exact Duplicates
# -------------------------

shutil.copy(
    os.path.join(INPUT_FOLDER, "article1.txt"),
    os.path.join(INPUT_FOLDER, "article1_copy.txt")
)

shutil.copy(
    os.path.join(INPUT_FOLDER, "article2.txt"),
    os.path.join(INPUT_FOLDER, "article2_duplicate.txt")
)

# -------------------------
# Similar but NOT Duplicate
# -------------------------

text4 = """Python is an amazing programming language.
It is used for AI, Machine Learning, Data Science!!

"""

with open(os.path.join(INPUT_FOLDER, "article1_modified.txt"), "w", encoding="utf-8") as f:
    f.write(text4)

text5 = """Artificial Intelligence is changing the world.
Machine Learning is a subset of AI.
Extra line added.
"""

with open(os.path.join(INPUT_FOLDER, "article2_modified.txt"), "w", encoding="utf-8") as f:
    f.write(text5)

# -------------------------
# Empty Files
# -------------------------

open(os.path.join(INPUT_FOLDER, "empty1.txt"), "w").close()

shutil.copy(
    os.path.join(INPUT_FOLDER, "empty1.txt"),
    os.path.join(INPUT_FOLDER, "empty2.txt")
)

# -------------------------
# Binary Files
# -------------------------

binary = os.urandom(2048)

with open(os.path.join(INPUT_FOLDER, "binary1.bin"), "wb") as f:
    f.write(binary)

with open(os.path.join(INPUT_FOLDER, "binary1_copy.bin"), "wb") as f:
    f.write(binary)

with open(os.path.join(INPUT_FOLDER, "binary2.bin"), "wb") as f:
    f.write(os.urandom(2048))

print("Duplicate test dataset created successfully.")


#  ye files banane ke liye

