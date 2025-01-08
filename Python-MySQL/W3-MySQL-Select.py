#MySQL - SELECT

import mysql.connector
from tabulate import tabulate

#connect database
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'user1',
    password = 'password2#',
    database = 'W3DB1'
)

#get cursor
mycursor = mydb.cursor()

#fetch records
mycursor.execute("SELECT * FROM customers")
records = mycursor.fetchall()

#format records to print - format 1
print("{0:<8}\t{1:<8}".format("Name","Address"))
for x in records:
    print("{0:<8}\t{1:<8}".format(x[1],x[2]))

#format and print using tabulate
headers = ['Name', 'Address']    

print(tabulate(records,headers,tablefmt="grid"))

mycursor.close()

#Fetch one record
try:

    mycursor = mydb.cursor(buffered=True)

    mycursor.execute("SELECT * FROM customers")

    records = mycursor.fetchone()

    print(tabulate([records],headers,tablefmt="grid"))
except Exception as e:
    print(f"Error occured: {e}")
finally:
    if(mycursor):
        mycursor.close()
    mydb.close()



