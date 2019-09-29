import MySQLdb

#MYSQL connection
connect = MySQLdb.connect(port = 1902, host='localhost', user='root', password='1234', database='mysql', charset='utf8')
cursor = connect.cursor()

try:
    cursor.execute("CREATE TABLE user (name VARCHAR(100) NOT NULL,\
        email VARCHAR(100) NOT NULL, sex VARCHAR(20) NOT NULL,  )")
        # 이름, 브랜드, 가격, 이미지, 카테고리, 세부카테고리
except MySQLdb._exceptions.OperationalError:
    print("already exist")