from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

#MYSQL connection
conn = pymysql.connect(port = 1902, host='localhost', user='root', password='1234', database='mysql', charset='utf8')



'''
html = urlopen("https://store.musinsa.com/app/contents/bestranking?u_cat_cd=001")
page = BeautifulSoup(html, "html.parser")

homepage = "https://store.musinsa.com"

ul = page.find("ul", {"class":"snap-article-list boxed-article-list article-list center list goods_small_media8"})

li = ul.find_all("li", {"class":"li_box"})

for l in li:
    div = l.find("div", {"class":"li_inner"})
    div = div.find("div", {"class":"list_img"})
    a = div.find("a", {"class":"img-block"})
    link = a['href']
    clothpage = homepage + str(link)

    currenthtml = urlopen(clothpage)
    currentpage = BeautifulSoup(currenthtml, "html.parser")
    title = currentpage.find("span",{"class":"product_title"})
    title = title.find("span").text     #이름
    itemcategory = currentpage.find("p",{"class":"item_categories"})
    info = itemcategory.find_all("a")
    brand = info[0].text        #브랜드
    subject = info[1].text      #품목
    category = info[2].text     #세부품목
    image = currentpage.find("div",{"class":"product-img"})
    image = image.find("img")
    image = image['src']        #이미지
 
    table = currentpage.find("table", {"class":"table_th_grey"}).find("tbody")
    table = table.find_all("tr")    
    table = table[2].find_all("td")
    length[] = table[0]       #총장
    shoulder[] = table[1] 어깨너비
    chest[] = table[2]        #가슴단면
    sleeve[] = table[3]       #소매길이  
'''



