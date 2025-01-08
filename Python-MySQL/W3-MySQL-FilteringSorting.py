#MySQL - Filtering, sorting, Delete
import mysql.connector
from tabulate import tabulate

#Connect database
mydb = mysql.connector.connect(
    host ='localhost',
    user = 'user1',
    password = 'password2#',
    database = 'W3DB1'
)

codesegment_execute = 5

try:
    #Get cursor
    mycursor = mydb.cursor()

    if codesegment_execute == 1:

        #Query for fetching records
        sql = "SELECT Name,Address FROM customers WHERE Address like %s"
        val = ('%Street%',)

        #execute query
        mycursor.execute(sql,val)

        #Fetch records
        records = mycursor.fetchall()

        #print records
        headers = ['Name','Address']

        print(tabulate(records,headers,tablefmt='grid'))
    elif codesegment_execute == 2:

        #Query for fetching records
        val = 'Street'
        sql = f"SELECT * FROM customers WHERE Address like '%{val}%'"
        print(f"sql:{sql}")

        #Execute records
        mycursor.execute(sql)

        #Fetch records
        records = mycursor.fetchall()

        #print records
        headers = ['Name','Address']

        print(tabulate(records,headers,tablefmt='grid'))
    elif codesegment_execute == 3:
        #use IN clause in query
        val = ['Street 21', 'Street 22', 'Street 23', 'Street 45']
        sql = "SELECT * FROM customers WHERE Address IN (%s)" % ','.join(['%s'] * len(val))
        #sql = "SELECT Name, Address FROM customers WHERE id IN ({})".format(','.join(['%s'] * len(val)))
        #sql = f"SELECT Name, Address FROM customers WHERE id IN ({','.join(['%s'] * len(val))})"
        #excute the query
        print(sql)
        mycursor.execute(sql,val)

        #fetch records
        records = mycursor.fetchall()

        #print records
        headers = ['Name','Address']
        print(tabulate(records,headers,tablefmt='grid'))
    elif codesegment_execute == 4:
        #use ORDER BY clause
        sql = "SELECT * FROM customers ORDER BY Name DESC"

        #excute the query
        mycursor.execute(sql)

        #fetch records
        records = mycursor.fetchall()

        #print records
        headers = ['Name','Address']
        print(tabulate(records,headers,tablefmt='grid'))
    elif codesegment_execute == 5:
        #use IN clause in query
        sql = "DELETE FROM customers WHERE Name = %s"
        val = ('Mike',)

        #excute the query
        mycursor.execute(sql, val)

        #commit changes
        mydb.commit()

        #print records        
        print(mycursor.rowcount,"records deleted")        
except Exception as e:
    print(f"Error occured: {e}")
finally:    
    mycursor.close()
    mydb.close()