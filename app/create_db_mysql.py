import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='gvg',
    passwd='passw1',
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE users_db")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)