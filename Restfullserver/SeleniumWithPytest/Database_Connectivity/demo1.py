import mysql.connector as connection

con = connection.connect(host='localhost', user='root', password='Raja@2688', database='raja')

if con.is_connected():
    print("MySQL Database is connected !!!!!")
else:
    print("Connectivity issue !!!!!")

con.close()

