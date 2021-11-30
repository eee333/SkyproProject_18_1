import hashlib
from flask import request, abort
import jwt
from constants import JWT_KEY, JWT_METHOD, PWD_HASH_SALT, PWD_HASH_ITERATIONS


def jwt_decode():
    if "Authorization" not in request.headers:
        abort(401, "Authorization Error")
    token = request.headers["Authorization"].split("Bearer ")[-1]
    try:
        decoded_jwt = jwt.decode(token, JWT_KEY, JWT_METHOD)
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
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),  # Convert the password to bytes
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ).decode("utf-8", "ignore")
