import http.client

print("--+ This program informs whether a resourse exists on the web server or not. +--")

host = input("Enter the target IP : ")
port = input("Enter the port number (default is 80) : ")
url = input("Enter the resource (default:/index.php) : ")

if(port == ""):
	port = 80

if(url == ""):
	url = r"/index.php"

try:
	connection = host.client.HTTPConnection(host, port)
	connection.request("GET", url)
	response = connection.getresponse()
	print("Server response is : ", response.status)
	connection.close()

except ConnectionRefusedError:
	print("Connection Failed...")