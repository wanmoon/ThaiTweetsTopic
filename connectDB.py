import mysql.connector

con = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='test',
                              port='8889')
print("can connect to db") #ต่อได้แล้วจ้า


con.close()