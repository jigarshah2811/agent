from flask import Flask, jsonify, abort, make_response, request, url_for
import time
import json
import logging
logger = logging.getLogger('WebSocketClient')

def configNetwork(request):
	logger.debug("Network configuration started...")
	time.sleep(1)
	logger.debug("Network configuration finished...")

	logger.debug("Prepare response to cloud...")
	response = {"api" : "configNetwork", "result": "SUCCESS"}
	return json.dumps(response, ensure_ascii=False)
