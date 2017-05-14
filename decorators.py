import json
from flask import Flask, jsonify, make_response, request, url_for
from functools import wraps
import logging

"""
Admin user can give commands
"""
authenticated_users = {
    "admin": "secret",
    "jigar": "secret"
}

logger = logging.getLogger('WebSocketClient')


def abort_operation(self, code):
    return json.dumps({"Abort": "Operation Aborted"}, ensure_ascii=False)

def validate_json(*expected_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:
                if expected_arg not in json_object:
                    abort_operation(400)
            return func(*args, **kwargs)

        return wrapper

    return decorator

class decoratorWithoutArguments(object):
    def __init__(self, func):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        logger.debug("__init__() of decoratorWithoutArguments")
        self.func = func

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        logger.debug("__call__() of decoratorWithoutArguments")
        request = args[1]
        request = json.loads(request)
        if self.get_password(request['username']) != request['password']:
            self.unauthorized()
        else:
            self.func(*args)

    def unauthorized(self):
        return json.dumps({"error": "UnAuthorized Access"}, ensure_ascii=False)

    def get_password(self, username):
        if username in authenticated_users:
            return authenticated_users.get(username)
        return None

    def abort_operation(self, code):
        return json.dumps({"Abort": "Operation Aborted"}, ensure_ascii=False)

class decoratorWithArguments(object):
    def __init__(self, ws, request):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        logger.debug("Inside __init__()")
        self.ws = ws
        self.request = request

    def __call__(self, func):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        logger.debug("Inside __call__()")

        def wrapped_func(*args):
            logger.debug("Inside wrapped_f()")
            logger.debug("Decorator arguments:{0} and {1}".format(self.ws, self.request))
            request = json.loads(self.request)
            if get_password(request['username']) != request['password']:
                self.unauthorized()
            else:
                func(*args)

        return wrapped_func

    def unauthorized(self):
        return json.dumps({"error": "UnAuthorized Access"}, ensure_ascii=False)

    def get_password(self, username):
        if username in authenticated_users:
            return authenticated_users.get(username)
        return None

    def abort_operation(self, code):
        return json.dumps({"Abort": "Operation Aborted"}, ensure_ascii=False)

