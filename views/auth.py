# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask import request
from flask_restx import Resource, Namespace
# from dao.auth import UserSchema
from implemented import auth_service

auth_ns = Namespace('auth')
# auth_schema = UserSchema()
# auths_schema = UserSchema(many=True)


@auth_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_auths = auth_service.get_all()
        return auths_schema.dump(all_auths), 200

    def post(self):
        req_json = request.json
        new_auth = auth_service.create(req_json)
        return f"Created id: {new_auth.id}", 201


