# Method 8 — Using Trafilatura (Industry Standard)

# Install

# pip install trafilatura

# Code

import trafilatura

with open("page.html","r",encoding="utf-8") as f:
    html = f.read()

text = trafilatura.extract(html)

print(text)

# Ye automatically

# Header
# Footer
# Navigation
# Ads
# Cookie banners
# Boilerplate

# remove karke sirf main article deta hai.