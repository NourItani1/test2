import pyodbc
server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT top 10 * from Person.Person")
row = cursor.fetchone()

x=[]
while row:
    x.append(row)
    print (row[0], row[4], row[6])
    row= cursor.fetchone()


n= input("Enter a name")
cursor.execute("Select * From Person.Person WHERE Firstname= \'" +n + "\'")

row = cursor.fetchone()
print(row)







