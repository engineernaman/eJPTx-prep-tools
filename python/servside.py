import socket

SRV_ADDR = input("Server's IP Address : ")
SRV_PORT = int(input("Server's Port : ")) 

s = socket.socket(socket_AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1) //1 is for maximux no of connections in queue = 1

print("Waiting for the connection...!!!")

connection, address = s.accept()
print("Someone with IP :", address, "has connected...")

while 1:
	data = connection.recv(1024)
	if not data: break
	connection.sendall(b'-- Message was Received --\n')
	print(data.decode('utf-8'))

connection.close()