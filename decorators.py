import json
from flask import Flask, jsonify, abort, make_response, request, url_for
from functools import wraps


authenticated_users = {
    "admin": "secret",
    "jigar": "secret"
}

"""
Admin user can give commands
"""
# auth = HTTPBasicAuth()
# @auth.get_password
def get_password(username):
	if username in authenticated_users:
		return authenticated_users.get(username)
	return None

def validate_json(*expected_args):
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			json_object = request.get_json()
			for expected_arg in expected_args:
				if expected_arg not in json_object:
					abort(400)
			return func(*args, **kwargs)
		return wrapper
	return decorator

def auth_required(func):
	def decorator(func):
		def wrapper(*args, **kwargs):
			request = json.loads(*args)
			if get_password(request['username']) != request['password']:
				unauthorized()
				return None
			func(*args, **kwargs)
		return wrapper
	return decorator


class decoratorWithoutArguments(object):

    def __init__(self, func):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print "Inside __init__()"
        self.f = func

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        request = args[1]
        request = json.loads(request)
        if get_password(request['username']) != request['password']:
            self.unauthorized()
        else:
            self.func(*args)

    # @auth.error_handler
    def unauthorized(self):
        return make_response(jsonify({"error": "UnAuthorized Access"}), 403)


class decoratorWithArguments(object):

    def __init__(self, ws, request):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print "Inside __init__()"
        self.ws = ws
        self.request = request

    def __call__(self, func):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print "Inside __call__()"
        def wrapped_func(*args):
            print "Inside wrapped_f()"
            print "Decorator arguments:", self.ws, self.request
            request = json.loads(self.request)
            if get_password(request['username']) != request['password']:
                self.unauthorized()
            else:
                func(*args)
        return wrapped_func

    # @auth.error_handler
    def unauthorized(self):
        return make_response(jsonify({"error": "UnAuthorized Access"}), 403)
