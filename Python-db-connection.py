import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",port='3306', passwd="Tekam@1234")

mycursor = mydb.cursor()
mycursor.execute("Show databases")

for db in mycursor:
    print(db)