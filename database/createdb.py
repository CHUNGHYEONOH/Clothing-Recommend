from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb
import re

#MYSQL connection
connect = MySQLdb.connect(port = 1902, host='localhost', user='root', password='1234', database='mysql', charset='utf8')
cursor = connect.cursor()

try:
    cursor.execute("CREATE TABLE service_review (image VARCHAR(100) NOT NULL,\
         title VARCHAR(50),  designer VARCHAR(100), \
        price INTEGER(15), score INTEGER(15))" )
except MySQLdb._exceptions.OperationalError:
    print("already exist")
