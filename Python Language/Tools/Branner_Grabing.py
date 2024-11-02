import socket

Client = socket.socket()
Client.connect(("192.168.0.108",22))

Received = Client.recv(1024)

print(reversed)

Client.close