"""
   * author - Akshay Tekam
   * date - 18/01/21
   * time - 10:23:44
   * package - socket, mysql-connector and threading
   * Title - Create a multi user chat application using socket and mysql DB.
"""

import os
import socket
from threading import Thread
import mysql.connector
# Connect to the database using root and password
var=os.environ.get('DB_USER')
var1=os.environ.get('DB_PASS')

mydb = mysql.connector.connect(host="localhost", user=var,port='3306', passwd=var1, database="akkidb")
mycursor = mydb.cursor()

name = input("Enter your name:")

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Connect socket at port 5555
client.connect(("localhost",5555))

client.send(name.encode())

# send function takes input from one client
# and send it to other
def send(client):
    while True:
        data = f'{name}:{input("")}'            # take input and send it to another client
        client.send(data.encode())

# receive function take msg from another
# client and put it into DB meanwhile
def receive(client):
    while True:
        try:
            data = client.recv(1024).decode()     # decode the received byte msg
            print(data)
            val = (name, data)
            mycursor.execute(sql, val)          # put values into database
            mydb.commit()
        except:
            client.close()
            break
sql = "Insert into room (name, chat) Values (%s, %s)"   # take the values

# Thread execute multiple process concurrently
thread1 = Thread(target=send, args=(client,))
thread1.start()
thread2 = Thread(target=receive, args=(client,))
thread2.start()