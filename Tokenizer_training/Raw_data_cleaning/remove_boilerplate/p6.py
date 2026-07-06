# Method 6 — Remove Header + Footer + Navigation
from bs4 import BeautifulSoup



with open("page.html","r",encoding="utf-8") as f:
    html = f.read()
soup = BeautifulSoup(html,"html.parser")

for tag in soup(["header","footer","nav"]):
    tag.decompose()

print(soup.get_text())

# Ye industry me bahut common hai.