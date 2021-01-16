from socket import *
from time import *

server=socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 1000))
server.listen()
print('Server listening.....')
connection, address =server.accept()
print('connected to client at '+ ctime())

while True:
    data =input('server: ')
    connection.send(bytes(data +" "+ctime(), 'utf-8'))
    recData =connection.recv(1024).decode()
    print("client: ", recData)

connection.close()