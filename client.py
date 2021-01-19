import socket
from threading import Thread
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",port='3306', passwd="Tekam@1234", database="akkidb")
mycursor = mydb.cursor()

name = input("Enter your name:")

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",1000))

client.send(name.encode())

def send(client):
    while True:
        data = f'{name}:{input("")}'            # take input and send it to another client
        client.send(data.encode())

def receive(client):
    while True:
        try:
            data = client.recv(1024).decode()
            print(data)
            val = (name, data)
            mycursor.execute(sql, val)          # put values into database
            mydb.commit()
        except:
            client.close()
            break
sql = "Insert into room (name, chat) Values (%s, %s)"   # take the values


thread1 = Thread(target=send, args=(client,))
thread1.start()
thread2 = Thread(target=receive, args=(client,))
thread2.start()

