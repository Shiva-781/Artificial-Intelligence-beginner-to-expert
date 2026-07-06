# Method 4 — Remove Navigation Menu



# Code

from bs4 import BeautifulSoup

with open("page.html","r",encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html,"html.parser")

for nav in soup.find_all("nav"):
    nav.decompose()

print(soup.get_text())

# Output

# Sample Website



# My Website



# Python Programming

#             Python is one of the most popular programming languages.
        

#             It is widely used in Artificial Intelligence,
#             Machine Learning, Data Science, Web Development,
#             and Automation.
        

#             Python has a simple syntax, making it easy to learn.
        


# Copyright © 2025 My Website













# Notice:

# ✅ Home
# ✅ About
# ✅ Services
# ✅ Blog
# ✅ Contact
# ✅ Privacy Policy
# ✅ Terms of Service

# sab remove ho gaye kyunki ye <nav> ke andar the.