# Method 5 — Complete Whitespace Normalization

# Ye NLP me bahut common hai.

# Code
import re

text = """
Hello


     World


Python\t\tis      awesome.
"""

# Tabs + spaces
text = re.sub(r"[ \t]+", " ", text)

# Blank lines
text = re.sub(r"\n{2,}", "\n\n", text)

# Remove leading/trailing whitespace
text = text.strip()

print(text)