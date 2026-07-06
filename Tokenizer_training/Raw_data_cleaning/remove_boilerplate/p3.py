# Method 3 — Remove HTML Tags

# Agar raw data HTML hai.

# Install

# pip install beautifulsoup4

# Code

from bs4 import BeautifulSoup

html = """

<html>

<body>

<h1>Python</h1>

<p>Python is awesome.</p>

</body>

</html>

"""

soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())

# Output

# Python
# Python is awesome.