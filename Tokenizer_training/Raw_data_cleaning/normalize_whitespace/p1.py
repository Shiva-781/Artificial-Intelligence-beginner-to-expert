# Method 1 — Multiple Spaces → Single Space

# Sirf multiple spaces ko single space me convert karta hai.

# Code
import re

text = "Hello          World"

clean = re.sub(r" +", " ", text)

print(clean)