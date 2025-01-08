#MySQL - Insert
import mysql.connector

#Connect to Database
mydb = mysql.connector.connect(
    host='localhost',
    user='user1',
    password='password2#',
    database = 'W3DB1'
)

codesegment_execute = 2

#Get cursor
mycursor = mydb.cursor()

if codesegment_execute == 1:

    #insert data into table customers
    sql = "INSERT INTO customers(name,address) VALUES(%s,%s)"
    val = ("John", "Highway 21")

    mycursor.execute(sql,val)

    mydb.commit()

    print(f"Inserted Record count: {mycursor.rowcount}")

elif codesegment_execute == 2:
    tablename = "products"

    if tablename == "customers":

        #insert multiple records in the customers table
        sql = "INSERT INTO customers(name,address) VALUES(%s,%s)"
        val = [
            ('Roy','Std Rd 121'),
            ('Henry', 'South Ave 34'),
            ('John', 'North Ave 54'),
            ('Kelly','East Ave 56'),
            ('Bob','West Ave 101'),
            ('Kim','Street 21'),
            ('Manu', 'Street 22'),
            ('Gill', 'Street 23'),
            ('Stuart', 'Street 45'),
            ('Allen', 'Street 78'),
            ('Bini', 'Street 84'),
            ('Vincent', 'Street 29'),
            ('David', 'Street 17')
        ]

        mycursor.executemany(sql, val)
        mydb.commit()

        print(f"Inserted record count: {mycursor.rowcount}")
    elif tablename == "users":

        #insert multiple records in the users table
        sql = "INSERT INTO users(id,Name,fav) VALUES(%s,%s,%s)"
        val = [
            (1,'Roy',154),
            (2,'David', 154),
            (3,'Stuart', 155),
            (4,'Kelly',None),
            (5,'Manu',None)
        ]

        mycursor.executemany(sql, val)
        mydb.commit()

        print(f"Inserted record count: {mycursor.rowcount}")

    elif tablename == "products":

        #insert multiple records in the products table
        sql = "INSERT INTO products(id,Name) VALUES(%s,%s)"
        val = [
            (154,'Chocolate Heaven'),
            (155,'Tasty Lemons'),
            (156,'Vanilla Dreams')
        ]

        mycursor.executemany(sql, val)
        mydb.commit()

        print(f"Inserted record count: {mycursor.rowcount}")
elif codesegment_execute == 3:
    #get rowid for last record inserted
    sql = "INSERT INTO customers(name, address) VALUES(%s, %s)"
    val = ("Mike", "Street 71")

    mycursor.execute(sql,val)

    mydb.commit()

    print(f"1 record inserted, ID: {mycursor.lastrowid}")

mycursor.close()
mydb.close()
