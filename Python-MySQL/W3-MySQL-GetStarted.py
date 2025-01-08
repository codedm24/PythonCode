#MySQL - Get Started
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sqlserver2025'
)

print(mydb)

#get cursor
mycursor = mydb.cursor()

#create a database
#mycursor.execute("CREATE DATABASE W3DB1")

#check if database created
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

