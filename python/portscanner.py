import socket

target = input("Enter the victim IP : ")
portrange = input("Enter the port range to scan (Format is 1 - 100): ")

lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print("Initiating the scan on {} from port {} to {}...".format(target, lowport, highport))

for port in range(lowport, highport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	status = s.connect_ex((target, port))
	if status == 0:
		print("---PORT {} is open.---".format(port))
	else:
		print("***PORT {} is closed.***".format(port))
		s.close()