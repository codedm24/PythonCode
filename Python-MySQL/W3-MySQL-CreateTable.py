#MySQL - Create Table
import mysql.connector
import sys

tablename = ['customers','users','products']
columns = [
    ['id','Name','Address'],
    ['id','Name','fav'],
    ['id','Name']
]
columntype = [
    ['INT AUTO_INCREMENT PRIMARY KEY', 'VARCHAR(255)', 'VARCHAR(255)'],
    ['INT PRIMARY KEY', 'VARCHAR(255)', 'INT'],
    ['INT PRIMARY KEY', 'VARCHAR(255)'],
]

#function to create a CREATE TABLE statement
def create_table_statement(tablename, columns, columntype):
    col_definitions = ','.join([f"{col} {ctype}" for col, ctype in zip(columns, columntype)])
    return f"CREATE TABLE {tablename} ({col_definitions})"

#create CREATE TABLE statement for each table
create_table_dict = {}

for table,cols,ctypes in zip(tablename,columns,columntype):
    statement = create_table_statement(table,cols,ctypes)
    create_table_dict[table] = statement

for table,statement in create_table_dict.items():
    print(f"{table}: {statement} ")

#sys.exit()

table_name = "products"
statement = create_table_dict[table_name]

#connect database
mydb = mysql.connector.connect(
    host='localhost',
    user='user1',
    password='password2#',
    database='W3DB1'
)

#Get a cursor
mycursor = mydb.cursor()

#Check if table exists
mycursor.execute("SHOW TABLES")

tablexists = False

for x in mycursor:
    print(f"Table:{x}")
    for index,value in enumerate(x):
        print(f"Item name: {index}, Value:{value}")
    for i in range(len(x)):
        print(f"Item name: {i}, Value: {x[i]}")        
    if x[0] == table_name:
        tablexists = True

if(tablexists == False):
    #mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    mycursor.execute(statement)
    print(f"Table {table_name} created")
else:    
    print(f"Table {table_name} already exists")        
    #mycursor.execute("DROP TABLE customers")
    #mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY_KEY")

mycursor.close()
mydb.close()
