#!/usr/bin/python
import json
import websocket
import ssl
from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify, abort, make_response, request, url_for
import time
import thread
import logging
from decorators import decoratorWithoutArguments, validate_json
from configNetwork import configNetwork
from getDeviceInfo import getDeviceInfo

agent_api_list = {
    'configNetworkApi': configNetwork,
    'getDeviceInfoApi': getDeviceInfo
}


def print_func(json_data):
    logger.debug("calling fun {0} for command {1}".format(agent_api_list[json_data['api']], json_data['api']))


def not_found(api):
    response = {"api": api, "result": "NOT FOUND"}
    return response


# @auth.login_required
# @validate_json('username')
@decoratorWithoutArguments
def on_message(ws, request):
    request = json.loads(request)
    logger.debug('on_message', request)

    # Client REST API
    api = request['api']
    if api not in agent_api_list:
        response = not_found(api)

    else:
        # Call relevent Function for this API
        print_func(request)
        response = agent_api_list[api](request)

    logging.debug("Sent to Cloud: {0}".format(response))
    ws.send(json.dumps(response, ensure_ascii=False))


def on_error(ws, error):
    logger.debug('on_error')
    logger.error(error)


def on_close(ws):
    logger.debug('on_close')
    logger.info("### closed ###")


def on_open(ws):
    logger.debug('on_open')

    def run(*args):
        for i in range(1):
            message = u"Hello Server"
            logging.debug("Sent to Cloud: {0}".format(message))
            ws.send(message)
            time.sleep(1)
        # ws.close()
        # print "thread terminating..."

    thread.start_new_thread(run, ())


def start_client():
    # server_url = u"wss://127.0.0.1:8000/"
    server_url = u"wss://54.190.43.131:8000/"
    ssl_opt = {
        'check_hostname': False,
        'ca_certs'      : 'server.crt'
    }

    # Use to debug Websocket connection failures
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(server_url,
                                on_message=on_message,
                                on_open=on_open,
                                on_close=on_close,
                                on_error=on_error,
                                keep_running=True)
    # conn = websocket.create_connection(server_url, sslopt=ssl_opt)
    logger.info('Agent Connecting to Cloud...')
    ws.run_forever(sslopt=ssl_opt)


if __name__ == "__main__":
    logging.basicConfig(filename='agent.log', filemode='w', level=logging.DEBUG,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logger = logging.getLogger('WebSocketClient')
    start_client()
