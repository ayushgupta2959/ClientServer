import socket

server = socket.socket()
print("socket created")

port = 5000

server.bind(('',port))

server.listen(2)

while(True):
	client,addr = server.accept()
	print("connection established with ",addr)
	message = "You are connected"
	client.send(message.encode())
	a = int(client.recv(1024))
	b = int(client.recv(1024))
	c = str(a+b)
	client.send(c.encode())
	client.close()
