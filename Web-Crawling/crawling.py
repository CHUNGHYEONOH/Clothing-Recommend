from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#MYSQL connection
connect = MySQLdb.connect(port = 1902, host='localhost', user='root', password='1234', database='mysql', charset='utf8')
cursor = connect.cursor()

try:
    cursor.execute("CREATE TABLE clothes (name VARCHAR(100) NOT NULL,\
        brand VARCHAR(50), price INT(15), image VARCHAR(100), category VARCHAR(30),\
        subcategory VARCHAR(30) )")
        # 이름, 브랜드, 가격, 이미지, 카테고리, 세부카테고리
except MySQLdb._exceptions.OperationalError:
    print("already exist")

connect.commit()

html = urlopen("https://store.musinsa.com/app/contents/bestranking?u_cat_cd=001")
page = BeautifulSoup(html, "html.parser")

homepage = "https://store.musinsa.com"

ul = page.find("ul", {"class":"snap-article-list boxed-article-list article-list center list goods_small_media8"})

li = ul.find_all("li", {"class":"li_box"})

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://store.musinsa.com/app/contents/bestranking?u_cat_cd=001')

# Enter next Page
pagenext = driver.find_element_by_css_selector("a.fa.fa-angle-right.paging-btn.btn.next")
pagenext.send_keys(Keys.ENTER)
pagenext.send_keys(Keys.ENTER)
pagenext.send_keys(Keys.ENTER)
print(driver.current_url)


'''
for l in li:
    rank = l.find("div", {"class":"icon_best"})
    rank = rank.text
    rank = re.findall('[0-9]', rank)
    rank = ''.join(rank)        #순위

    div = l.find("div", {"class":"li_inner"})
    div = div.find("div", {"class":"list_img"})
    a = div.find("a", {"class":"img-block"})
    link = a['href']
    clothpage = homepage + str(link)

    currenthtml = urlopen(clothpage)
    currentpage = BeautifulSoup(currenthtml, "html.parser")
    name = currentpage.find("span",{"class":"product_title"})
    name = name.find("span").text     #이름
    itemcategory = currentpage.find("p",{"class":"item_categories"})
    info = itemcategory.find_all("a")
    brand = info[0].text        #브랜드
    category = info[1].text      #품목
    subcategory = info[2].text     #세부품목
    image = currentpage.find("div",{"class":"product-img"})
    image = image.find("img")
    image = image['src']        #이미지
    price = currentpage.find("span", {"class":"product_article_price"})
    price = price.text        #가격
    price = re.findall('[0-9]', price)
    price = ''.join(price)
    DATA = "INSERT INTO clothes VALUES (" + "'" + name + "'" + ", " + "'" + brand\
        + "'" + ", " + "'" + price + "'" + ", " + "'" + image + "'" +  ", "\
        + "'" + category + "'" + ", " + "'" + subcategory + "'" + ")"
    try:
        cursor.execute(DATA)
    except:
        print(name+brand+category)
    # 이름, 브랜드, 가격, 이미지, 카테고리, 세부카테고리
'''
'''
    table = currentpage.find("table", {"class":"table_th_grey"}).find("tbody")
    table = table.find_all("tr")    
    table = table[2].find_all("td")
    length[] = table[0]       #총장
    shoulder[] = table[1] 어깨너비
    chest[] = table[2]        #가슴단면
    sleeve[] = table[3]       #소매길이  
'''
connect.commit()

cursor.close()
connect.close()