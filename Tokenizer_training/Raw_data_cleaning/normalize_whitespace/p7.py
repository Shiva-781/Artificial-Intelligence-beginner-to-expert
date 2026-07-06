# Method 7 — Function Version (Reusable)

import re

def normalize_whitespace(text):

    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(r"\n{2,}", "\n\n", text)

    return text.strip()


sample = """
Hello


World      Python
"""

print(normalize_whitespace(sample))