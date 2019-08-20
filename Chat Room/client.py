import socket
import select
import sys

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = int(sys.argv[1])
client.connect(('127.0.0.1',port))
msg = client.recv(1024)
print(msg)
print("enter empty to terminate connection")
while(True):
	msg=""
	msg = sys.stdin.readline()
	if(len(msg)==0):
		client.close()
	client.send(msg)