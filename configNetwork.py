from flask import Flask, jsonify, abort, make_response, request, url_for
import time
import json
import logging
logger = logging.getLogger('WebSocketClient')

def configNetwork(request):
	"""
		json_request = json.loads(request)
		if json_request['username'] == 'admin' and json_request['password'] == 'pass':

			ws.send("welcome Mr. admin")
		else:
			ws.send("you are not Mr. admin")
		"""
	logger.debug("Network configuration started...")
	time.sleep(1)
	logger.debug("Network configuration finished...")
	return json.dumps({"configNetwork": "SUCCESS"}, ensure_ascii=False)
