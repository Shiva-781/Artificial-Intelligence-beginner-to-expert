# Method 3 — Multiple Spaces + Tabs

# Ye sabse common method hai.

# Code
import re

text = "Hello\t\t     World      Python"

clean = re.sub(r"[ \t]+", " ", text)

print(clean)