import socket

SERV_ADDR = input("Enter the server's IP address : ")
SERV_PORT = int(input("Enter the server's listening port : "))

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((SERV_ADDR, SERV_PORT))
print("Connected to the server...")

message = input("Enter the message for the server : ")
my_sock.sendall(message.encode())
my_sock.close()