from socket import *
from time import *

client =socket()                            # Create socket
client.connect(('localhost', 1000))         # Connect to server
print('connected to server at '+ ctime())

while True:
    recData =client.recv(1024).decode()     # receive data in bytes and decode it
    print('server: ', recData)
    data =input('client:')                  # give input or reply
    client.send(bytes(data+" "+ctime(), 'utf-8'))
    print('Data sent')

client.close()