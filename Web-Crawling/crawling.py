from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://store.musinsa.com/app/contents/bestranking?u_cat_cd=001")
page = BeautifulSoup(html, "html.parser")

ul = page.find("ul", {"class":"snap-article-list boxed-article-list article-list center list goods_small_media8"})

li = ul.find_all("li", {"class":"li_box"})

top_name = []



for l in li:
    div = l.find("div", {"class":"li_inner"})
    div = div.find("div", {"class":"article_info"})
    p = div.find("p", {"class":"item_title"})
    a = p.find("a").text
    print(str(a))

