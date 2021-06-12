import socket, platform, os

SRV_ADDR = input("Enter the source address...")
SRV_PORT = 4433

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)

connection, address = s.accept()

while 1:
	try:
		data = connection.recv(1024)
	except:continue

	if(data.secode('utf-8') == '1'):
		tosend = platform.platform() + " " + platform.machine()
		connection.sendall(tosend.encode())
	elif(data.decode('utf-8') == '2'):
		data = connection.recv(!024)
		try:
			filelist = os.listdir(data.decode('utf-8'))
			tosend = ""
			for x in filelist:
				tosend += ", " + x
		except:
			tosend = "Wrong path"

		connectiom.sendall(tosend.encode())
	elif(data.decode('utf-8') == '0'):
		connection.close()
		connection, address = s.accept()


