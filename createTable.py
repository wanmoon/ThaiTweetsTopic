import mysql.connector

con = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='test',
                              port='8889')
print("can connect to db") #ต่อได้แล้วจ้า

#create cursor
cursor = con.cursor()

#create table
cursor.execute("CREATE TABLE `employees`(`first_name` varchar(14) NOT NULL,`last_name` varchar(16) NOT NULL)")

print("create table leaw ja")

cursor.close()
con.close()