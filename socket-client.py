#!/usr/bin/python 

import socket #import socket module

s = socket.socket() #create a socket object
# host = socket.gethostname()
host = "54.212.193.101"
port = 9001 #Reserve a port for your service

print host, port
s.connect((host,port))
print s.recv(1024)
s.close
