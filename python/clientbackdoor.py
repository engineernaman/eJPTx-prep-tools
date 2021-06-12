import socket

SRV_ADDR = input("Enter the IP address of ther server : ")
SRV_PORT = input("Enter the Server's listening Port : ")

def print_menu():
	print("""\n\nENter your choice from below menu: -
		1. Get system info.
		2. List thr directory contents.""")
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((SRV_ADDR, SRV_PORT))

print("Connection Established...")
print_menu()

while 1:
	message = input("Enter your choice  : ")

	if (message == "0"):
		my_sock.sendall(message.encode())
		my_sock.close()
		break
	elif (message == "1"):
		my_sock.sendall(message.encode())
		data = my_sock.recv(1024)
		if not data: break
		print(data.decode("utf-8"))
	elif (message == "2"):
		path = input("Enter the path : ")
		my_sock.sendall(message.encode())
		my_sock.sendall(path.encode())
		data = my_sock.recv(1024)
		data = data.decode("utf-8").split(",")
		print("*" * 40)
		for x in data:
			print(x)
		print("-" * 40)

	print_menu()