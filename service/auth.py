import base64
import calendar
import datetime
import hashlib
import hmac

from flask import request, abort
import jwt
from constants import JWT_SECRET, JWT_ALGORITHM, PWD_HASH_SALT, PWD_HASH_ITERATIONS



def jwt_decode():
    if "Authorization" not in request.headers:
        abort(401, "Authorization Error")
    token = request.headers["Authorization"].split("Bearer ")[-1]
    try:
        decoded_jwt = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
    except Exception as e:
        abort(401, f'JWT Decode Exception: {e}')
    else:
        return decoded_jwt


def auth_required(func):
    def wrapper(*args, **kwargs):
        jwt_decode()
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        decoded_jwt = jwt_decode()
        role = decoded_jwt.get("role")
        if role != "admin":
            abort(401, "Admin role required")
        return func(*args, **kwargs)
    return wrapper


def get_hash(password):
    return base64.b64encode(hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ))


def generate_token(data):
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
    data["exp"] = calendar.timegm(days130.timetuple())
    refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {'access_token': access_token, 'refresh_token': refresh_token}


def compare_passwords(password_hash, other_password):
    return hmac.compare_digest(
        base64.b64decode(password_hash),
        hashlib.pbkdf2_hmac('sha256', other_password.encode('utf-8'), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
    )