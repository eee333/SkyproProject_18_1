# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask import request
from flask_restx import Resource, Namespace
from dao.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):
        req_json = request.json
        new_user = user_service.create(req_json)
        return f"Created id: {new_user.id}", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid: int):
        user = user_service.get_one(uid)
        if user:
            return user_schema.dump(user), 200
        return "", 404

    def put(self, uid: int):
        req_json = request.json
        if not req_json.get('id'):
            req_json['id'] = uid
        if user_service.update(req_json) == 201:
            return f"Updated id: {uid}", 201
        return "not found", 404

    def delete(self, uid: int):
        if user_service.delete(uid) == 204:
            return "", 204
        return "not found", 404
