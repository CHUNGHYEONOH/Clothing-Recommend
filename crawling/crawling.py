from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb
import re

html = urlopen("https://www.mrporter.com/en-kr/mens/clothing")
page = BeautifulSoup(html, "html.parser")

homepage = "https://www.mrporter.com"

li = page.find_all("li",{"class":"pl-categories__item pl-categories__item--has-children"})

for l in li:
    categoryinfo = l.find("a",{"class":"pl-categories__link"})
    category = categoryinfo.text        #카테고리
    categorypage = categoryinfo['href']
    categorypage = homepage + categorypage
    print(categorypage)
    currenthtml = urlopen(categorypage)
    currentpage = BeautifulSoup(currenthtml, "html.parser")

    cloth = page.find_all("li", {"class":"pl-products-item"})

    for cl in cloth:
        a = cl.find("a", {"class":"pl-products-item__link"})
        link = a['href']
        clothpage = homepage+link #each pages url
        currenthtml = urlopen(clothpage)
        currentpage = BeautifulSoup(currenthtml, "html.parser")
        
        name = currentpage.find("span",{"class":"product-details__name"})
        name = name.find("span").text       #이름
        
        designer = currentpage.find("span",{"class":"product-details__designer"})
        designer = designer.find("span").text       #디자이너

        price = currentpage.find("span",{"class":"product-details__price--value price-sale"}).text
        
        image = currentpage.find("img", {"class":"product-image product-image__main"})
        image = image['src']        #사진

        ul = currentpage.find("ul",{"class":"product-accordion__list"})
        li = ul.find_all("li")
        description = ""
        for l in li:
            description += l.text       #설명
        #print(name + " " + category)

        color = currentpage.find("div",{"class":"product-colour--single threeSelectionItems"})
        color = color.find("p")
        color = color.text
        #print(color)