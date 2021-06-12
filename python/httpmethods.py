import http.client

print("--+ This program lists the methos available to interact with web server, if OPTIONS is enables. +--")

host = input("Enter the target IP : ")
port = input("Enter the port number (default is 80) : ")

if(port == ""):
	port = 80

try:
	connection = http.client.HTTPConnection(host, port)
	connection.request('OPTIONS', '/')
	response = connection.getresponse()
	print("Methods that are enabled are : ", response.getheader('allow'))
	connection.close()

except ConnectionRefusedError:
	print("Connection Failed")
