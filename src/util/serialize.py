from flask import jsonify
from functools import wraps


def http_code(code: int = 200):
    def out_decorator(f):
        @wraps(f)
        def in_decorator(*args, **kwargs):
            data = f(*args, **kwargs)
            resp = {"data": data, "code": code}
            return jsonify(resp), code

        return in_decorator

    return out_decorator
