import socket
import socketio
import socketengine
from threading import Thread
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",port='3306', passwd="Tekam@1234", database="akkidb")
mycursor = mydb.cursor()

io.sockets.on('connection', function (socket) {
  socket.join('a room');
  socket.broadcast.to('a room').send('im here');
  io.sockets.in('some other room').emit('hi');
});

name = input("Enter your name:")

mycursor.execute("SELECT * FROM room")
myresult = mycursor.fetchall()

for i in myresult:
	print(str(i))

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",5555))

client.send(name.encode())

def send(client):
    while True:
        data = f'{name}:{input("")}'
        client.send(data.encode())

def receive(client):
    while True:
        try:
            data = client.recv(1024).decode()
            print(data)
            val = (name, data)
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            client.close()
            break
sql = "Insert into room (name, chat) Values (%s, %s)"


thread1 = Thread(target=send, args=(client,))
thread1.start()
thread2 = Thread(target=receive, args=(client,))
thread2.start()

