# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from marshmallow import fields, Schema
from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def create(self, data_in):
        obj = User(**data_in)
        self.session.add(obj)
        self.session.commit()
        return obj

    def update(self, data_in):
        obj = self.get_one(data_in.get('id'))
        if obj:
            if data_in.get('name'):
                obj.name = data_in.get('name')
            self.session.add(obj)
            self.session.commit()
            return 201
        return 404

    def delete(self, uid):
        obj = self.get_one(uid)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            return 204
        return 404


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
