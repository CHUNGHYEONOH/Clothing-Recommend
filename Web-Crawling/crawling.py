from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://store.musinsa.com/app/contents/bestranking?u_cat_cd=001")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject)
