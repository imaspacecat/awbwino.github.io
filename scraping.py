import requests as req
from bs4 import BeautifulSoup, Tag
import uwuify

# page = req.get("https://www.linkedin.com/in/gregory-albrino-fernando-b11a28169")
# print(page.text)
contents = ""
with open('linkedin.html', 'r') as f:

    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

flags = uwuify.SMILEY | uwuify.YU
for tag in soup.find_all(["p", "h1", "h2", "h3"]):
  tag.string = uwuify.uwu(tag.next, flags=flags)

for a in soup.find_all("a"):
  a["href"] = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  a["target"] = "_blank"

print(soup.contents)
