from flask import Flask, jsonify, abort, make_response, request, url_for

def configCam(request):
	"""
		json_request = json.loads(request)
		if json_request['username'] == 'admin' and json_request['password'] == 'pass':

			ws.send("welcome Mr. admin")
		else:
			ws.send("you are not Mr. admin")
		"""
	print "Camera configuration started..."
	print "Camera configuration finished..."
	return make_response(jsonify({"configCam": "SUCCESS"}))
