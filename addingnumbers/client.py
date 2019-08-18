import socket

client = socket.socket()
port = 5000
client.connect(('127.0.0.1',port))

print("received message: ",client.recv(1024))
a = str(1)
b = str(2)
client.send(a.encode())
client.send(b.encode())
print("received sum: ",client.recv(1024))

client.close()
print("connection closed")