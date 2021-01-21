"""
   * author - Akshay Tekam
   * date - 18/01/21
   * time - 10:23:44
   * package - socket, mysql-connector and threading
   * Title - Create a multi user chat application using socket and mysql DB.
"""

import socket
from time import *
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Connect socket at port 5555
server.bind(("localhost",5555))

server.listen()                                                # put server in listen mode

# Put all users into Dictionary
all_clients = {}

# This function takes the input msg from a client
# and broadcast it to all other clients connected to server
# except one from who it received msg
def client_thread(client):
    while True:
        try:
            msg = client.recv(1024)                           # received msg
            for c in all_clients:
                c.send(msg)
        except:
            for c in all_clients:                             # send to all except receiver
                if c != client:
                    # show notification when to leave chat
                    c.send(f"{name} has left the chat at + {ctime()}".encode())

            del all_clients[client]                            # delete the client from dict. when he leave the chat
            client.close()
            break


while True:
    print("waiting for connection....")
    client, address = server.accept()                          # accept request from client to establish connection
    print("connection established!")

    name = client.recv(1024).decode()
    all_clients[client] = name

    for c in all_clients:
        if c != client:                                       # Notify when user joins the chat
            c.send(f"{name} has joined the chat at {ctime()}".encode())
    thread = Thread(target=client_thread,args=(client,))         # start thread
    thread.start()