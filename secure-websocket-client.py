#!/usr/bin/python
import json
import websocket
import ssl
from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify, abort, make_response, request, url_for
import time
import thread
from decorators import decoratorWithoutArguments, validate_json
from configNetwork import configNetwork

fun_dict = {
	'configNetworkCmd':configNetwork
}

def print_func(json_data):
	print "calling fun {0} for command {1}".format(fun_dict[json_data['msg']], json_data['msg'])

def not_found(cmd):
	return make_response(jsonify({'error': 'Bad Request'}), 400)

# @auth.login_required
# @validate_json('username')
# @decoratorWithoutArguments
def on_message(ws, request):
	print request
	request = json.loads(request)
	cmd = request['msg']
	if cmd not in fun_dict:
		not_found(cmd)

	# REST API, Call relevent API for this command
	print_func(request)
	response = fun_dict[cmd](request)
	ws.send(response)

def on_error(ws, error):
	print error

def on_close(ws):
	print "### closed ###"

def on_open(ws):
	print "on_open"
	def run(*args):
		for i in range(1):
			ws.send(u"Hello {0}".format(i))
			time.sleep(1)
			# ws.close()
			print "thread terminating..."
	thread.start_new_thread(run, ())

def start_client():
	"""
	# TODO: Secure connection: wss instead of ws

    certfile = "cert.pem"
    keyfile = "key.pem"
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ssl_context.load_cert_chain(certfile, keyfile)
    ws = create_connection("ws://34.210.26.95:9001/", sslopt={"cert_reqs": ssl.CERT_NONE, "check_hostname": False})
    """
	# TODO: Change to secure connection with AWS
	# server_url = u"wss://127.0.0.1:8000/"
	server_url = u"wss://54.190.43.131:8000/"

	ssl_opt = {
		'check_hostname' : False,
		'ca_certs' : 'server.crt'
	}

	# conn = websocket.create_connection(server_url, sslopt=ssl_opt)

	websocket.enableTrace(True)
	ws = websocket.WebSocketApp(server_url,
								on_message=on_message,
								on_open=on_open,
								on_close=on_close,
								on_error=on_error,
								keep_running=True)
	print "Connecting..."
	ws.run_forever(sslopt=ssl_opt)


if __name__ == "__main__":
	start_client()
