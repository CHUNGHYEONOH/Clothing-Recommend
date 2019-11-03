import MySQLdb

#MYSQL connection
connect = MySQLdb.connect(port = 1902, host='localhost', user='root', password='1234', database='mysql', charset='utf8')
cursor = connect.cursor()

a = {}

try:
    cursor.execute("SELECT userid, title, score FROM service_review")
    for row in cursor:
        if row[0] not in a:
            a[row[0]] = {}        
            print(a)
            a[row[0]][row[1]] = row[2]
        elif row[0] in a:
            a[row[0]][row[1]] = row[2]
    print(a)
except MySQLdb._exceptions.OperationalError:
    print("already exist")


