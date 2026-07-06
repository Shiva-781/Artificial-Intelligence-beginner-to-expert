# Method 2 — Remove Using Regular Expressions

# Agar boilerplate thoda different format me ho.

# Code
import re

text = """
Privacy Policy

Copyright 2025

Subscribe Now

Python is awesome.
"""

patterns = [
    r"Privacy Policy",
    r"Copyright.*",
    r"Subscribe.*"
]

for pattern in patterns:
    text = re.sub(pattern, "", text)

print(text)

# Output

# Python is awesome.