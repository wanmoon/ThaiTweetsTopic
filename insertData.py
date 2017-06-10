import mysql.connector

con = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='test',
                              port='8889')
print("can connect to db") #ต่อได้แล้วจ้า

#create cursor
cursor = con.cursor()

#insert data
cursor.execute("insert into `employees`(`first_name`,`last_name`) value('wc','wanmoon')")

print("insert data leaw ja")

con.commit()
cursor.close()
con.close()