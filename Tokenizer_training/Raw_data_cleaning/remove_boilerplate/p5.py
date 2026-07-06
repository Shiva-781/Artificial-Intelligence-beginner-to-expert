# Method 5 — Remove Footer
from bs4 import BeautifulSoup


with open("page.html","r",encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html,"html.parser")

for footer in soup.find_all("footer"):
    footer.decompose()

print(soup.get_text())