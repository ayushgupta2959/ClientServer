import socket
import select 
import sys
from thread import *

server = socket.socket()

port = 5001

server.bind(('',port))

server.listen(10)

clients = []

def braodcast(msg,conn):
	to_remove = []
	for client in clients:
		if(client!=conn):
			try:
				client.send(msg)
			except:
				client.close()
				to_remove.append(client)

	for client in to_remove:
		clients.remove(client)

def client_thread(conn,addr):
	conn.send("Joined chat room successfully")

	while(True):
		try:
			msg = conn.recv(2048)
			if(msg):
				print(addr[0]," -> ",msg)
				to_send = str(addr[0]) + " -> " + msg
				broadcast(to_send,conn)

			else:
				remove(conn)

		except:
			continue




while(True):
	client,addr = server.accept()

	broadcast(str(addr[0])+"joined the room",null)

	print(str(addr[0])+"is connected")

	start_new_thread(client_thread,(conn,addr))

conn.close()
server.close()

