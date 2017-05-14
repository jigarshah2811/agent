from flask import Flask, jsonify, abort, make_response, request, url_for
import time
import json

def configNetwork(request):
	"""
		json_request = json.loads(request)
		if json_request['username'] == 'admin' and json_request['password'] == 'pass':

			ws.send("welcome Mr. admin")
		else:
			ws.send("you are not Mr. admin")
		"""
	print "Network configuration started..."
	time.sleep(1)
	print "Network configuration finished..."
	return json.dumps({"configNetwork": "SUCCESS"}, ensure_ascii=False)

