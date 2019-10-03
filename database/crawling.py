from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb
import re

#MYSQL connection
connect = MySQLdb.connect(port = 1902, host='localhost', user='root', password='1234', database='mysql', charset='utf8')
cursor = connect.cursor()

try:
    cursor.execute("CREATE TABLE clothes (name VARCHAR(100) NOT NULL,\
        designer VARCHAR(50), price INTEGER(15), image VARCHAR(100), \
        category VARCHAR(30), color VARCHAR(30) )")
        # 이름, 브랜드, 가격, 이미지, 카테고리, 세부카테고리
except MySQLdb._exceptions.OperationalError:
    print("already exist")

html = urlopen("https://www.mrporter.com/en-kr/mens/clothing")
page = BeautifulSoup(html, "html.parser")

homepage = "https://www.mrporter.com"

li = page.find_all("li",{"class":"pl-categories__item pl-categories__item--has-children"})

for l in li:
    categoryinfo = l.find("a",{"class":"pl-categories__link"})
    category = categoryinfo.text        #카테고리
    categorypage = categoryinfo['href']
    categorypage = homepage + categorypage
    currenthtml = urlopen(categorypage)
    currentpage = BeautifulSoup(currenthtml, "html.parser")
    cloth = currentpage.find_all("li", {"class":"pl-products-item"})
    
    for cl in cloth:
        a = cl.find("a", {"class":"pl-products-item__link"})
        link = a['href']
        clothpage = homepage+link #each pages url
        currenthtml = urlopen(clothpage)
        currentpage = BeautifulSoup(currenthtml, "html.parser")
        
        try:
            name = currentpage.find("span",{"class":"product-details__name"})
            name = name.find("span").text       #이름
        except:
            print("name")
            continue
        
        try:
            designer = currentpage.find("span",{"class":"product-details__designer"})
            designer = designer.find("span").text       #디자이너
        except:
            print("designer")
            continue
        
        try:
            price = currentpage.find("span",{"class":"product-details__price--local price-sale"}).text
        except:
            print("price")
            continue

        try:
            image = currentpage.find("img", {"class":"product-image product-image__main"})
            image = image['src']        #사진
        except:
            print("image")
            continue
        
        '''
        try:
            ul = currentpage.find("ul",{"class":"product-accordion__content--inner"})
            li = ul.findall("li")
            description = ""
            for l in li:
                description += l.text       #설명
        except:
            print("description")
            continue
        '''

        try:
            color = currentpage.find("div",{"class":"product-colour--single threeSelectionItems"})
            color = color.find("p")
            color = color.text      
            color = color[8:]       #색깔
        except:
            print("color")
            continue
        
        clothsize = {"XS":'', "S":'', "M":'', "L":'', "XL":'', "XXL":''}

        try:
            select = currentpage.find("select",{"class":"select-option-style"})
            option = select.find_all("option")
            for op in option:
                size = op.text
                size = size.split(' ')
                if size[0] == "Select":
                    continue
                elif len(size) > 1 and size[2] == "Sold":
                    continue
                else:
                    size = size[0]
        except:
            print("size")
            continue

        price = re.findall('[0-9]',price)
        price = ''.join(price)
        price = int(price)
        price = price/100
        price = int(price)
        print(price)

        
        DATA = "INSERT INTO clothes VALUES (" + "'" + name + "'" + ", " + "'" + designer \
        + "'" + ", " + "'" + str(price) + "'" + ", " + "'" + image + "'" +  ", "\
        + "'" + category + "'" + ", " + "'" + color + "'" + ")"
        
        try:
            cursor.execute(DATA)
            print(name)
        except:
            print(name+designer+category)

connect.commit()

cursor.close()
connect.close()    