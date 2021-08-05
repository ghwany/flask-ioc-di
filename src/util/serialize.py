from flask import jsonify
from functools import wraps
from sqlalchemy.exc import DatabaseError


class HttpError(Exception):
    def __init__(self, message: str, code: int = 500):
        self.message = message
        self.code = code


def http_code(code: int = 200):
    def out_decorator(f):
        @wraps(f)
        def in_decorator(*args, **kwargs):
            resp = {}
            try:
                resp["data"] = f(*args, **kwargs)
            except HttpError as e:
                resp["error"], resp["code"] = e.message, e.code
            except DatabaseError as e:
                resp["error"], resp["code"] = "DatabaseError", 500
            except Exception as e:
                resp["error"], resp["code"] = "InternalServerError", 500
                print(e)
            else:
                resp["code"] = code
            return jsonify(resp), resp["code"]

        return in_decorator

    return out_decorator
