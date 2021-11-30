# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask import request
from flask_restx import Resource, Namespace
from service.auth import generate_token, compare_passwords
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
        print(pass_hashed)
        print(user_pass)
        if compare_passwords(pass_hashed, user_pass):
            tokens = generate_token(req_json)
            return tokens, 200
        return "Wrong password", 401


