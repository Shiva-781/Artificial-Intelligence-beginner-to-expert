# Method 4 — Remove Extra Blank Lines

# Example

# Hello


# World




# Python

# ↓

# Hello

# World

# Python



# Code
import re

text = "Hello\n\n\nWorld\n\n\n\nPython"

clean = re.sub(r"\n{2,}", "\n\n", text)

print(clean)