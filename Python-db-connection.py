import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",port='3306', passwd="Tekam@1234", database="akkidb")

mycursor = mydb.cursor()

mycursor.execute("select * from room")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
