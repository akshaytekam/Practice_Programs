import socket  # for socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1025))
s.listen(5)
while True:
    clt, adr=s.accept()
    print(f"Connection to {adr} established")
    clt.send(bytes("socket programming", "utf-8"))
    clt.close()