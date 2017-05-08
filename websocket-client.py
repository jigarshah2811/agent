#!/usr/bin/python
import json
from websocket import create_connection

def configCam_func(data, ws):
	print data
	json_data = json.loads(data)
	if json_data['username'] == 'admin' and json_data['password'] == 'pass':
        	ws.send("welcome Mr. admin")
	else:
		ws.send("you are not Mr. admin")

fun_dict = {
	'configCam':configCam_func
}

ws = create_connection("ws://34.210.26.95:9001/")
print "Sending 'Hello, World'..."
ws.send("Hello, World")
print "Sent"

while(1):
	print "Receiving..."
	result =  ws.recv()
	print "Received '%s'" % result
	json_data = json.loads(result)
	print json_data
	if json_data['msg'] == 'configCam':
		fun_dict[json_data['msg']](result, ws)
ws.close()
