# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask import request, abort
from flask_restx import Resource, Namespace
from service.auth import generate_token, compare_passwords, jwt_decode
from implemented import user_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):

    def post(self):
        req_json = request.json
        if not req_json:
            return "Authorization error", 401
        user_name = req_json.get("username")
        user = user_service.get_filter({"username": user_name})
        if not user:
            return "User not found", 401
        user_pass = req_json.get("password")
        pass_hashed = user[0].password
        req_json["role"] = user[0].role
        if compare_passwords(pass_hashed, user_pass):
            tokens = generate_token(req_json)
            return tokens, 200
        return "Wrong password", 401

    def put(self):
        req_json = request.json
        if not req_json:
            abort(401, "Authorization Error")
        refresh_token = req_json.get("refresh_token")
        data = jwt_decode(refresh_token)
        if data:
            tokens = generate_token(data)
            return tokens, 200
        abort(401, "Authorization Error")
