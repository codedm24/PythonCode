#MySQL - Drop, Update, Limit, Join
import mysql.connector
from tabulate import tabulate

#Connect database
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'user1',
    password='password2#',
    database = 'W3DB1'
)

codesegment_execute = 6

mycursor = mydb.cursor()

try:

    if codesegment_execute == 1: # DROP table
        
        #delete query statement
        sql = "DROP TABLE IF EXISTS customers"

        #execute query
        mycursor.execute(sql)

        print("Table dropped")

    elif codesegment_execute == 2: #UPDATE records
        #update statement
        sql = "UPDATE customers SET Address = %s WHERE id=%s"
        val = ('Avenue 71', 16)
        
        #execute sql
        mycursor.execute(sql,val)

        #commit database
        mydb.commit()

        #print records affected
        print(mycursor.rowcount,"record(s) affected")

    elif codesegment_execute == 3: #LIMIT records fetched WITH OFFSET
        #select statement
        sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"
        
        #execute sql
        mycursor.execute(sql)

        #fetch records
        myresult = mycursor.fetchall()

        #print records affected
        headers=['Name','Address']
        print(tabulate(myresult,headers,tablefmt='grid'))     

    elif codesegment_execute == 4: #INNER JOIN tables
        #select statement
        sql = "SELECT \
            users.name AS user, \
            products.name as favorite \
            FROM users \
            INNER JOIN products ON users.fav = products.id"
        
        #execute sql
        mycursor.execute(sql)

        #fetch records
        myresult = mycursor.fetchall()

        #print records affected
        headers=['User','Favorite']
        print(tabulate(myresult,headers,tablefmt='grid'))     

    elif codesegment_execute == 5: #LEFT JOIN tables
        #select statement
        sql = "SELECT \
            users.name AS user, \
            products.name as favorite \
            FROM users \
            LEFT JOIN products ON users.fav = products.id"
        
        #execute sql
        mycursor.execute(sql)

        #fetch records
        myresult = mycursor.fetchall()

        #print records affected
        headers=['User','Favorite']
        print(tabulate(myresult,headers,tablefmt='grid'))  

    elif codesegment_execute == 6: #RIGHT JOIN tables
        #select statement
        sql = "SELECT \
            users.name AS user, \
            products.name as favorite \
            FROM users \
            RIGHT JOIN products ON users.fav = products.id"
        
        #execute sql
        mycursor.execute(sql)

        #fetch records
        myresult = mycursor.fetchall()

        #print records affected
        headers=['User','Favorite']
        print(tabulate(myresult,headers,tablefmt='grid'))                      

except Exception as e:
    print(f"Error occured: {e}")
finally:
    mycursor.close()
    mydb.close()    