# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from service.auth import get_hash


class UserService:

    def __init__(self, user_dao):
        self.user_dao = user_dao

    def get_all(self):
        return self.user_dao.get_all()

    def get_one(self, uid):
        return self.user_dao.get_one(uid)

    def create(self, data_in):
        user_pass = data_in.get("password")
        if user_pass:
            data_in["password"] = get_hash(user_pass)
        return self.user_dao.create(data_in)

    def update(self, data_in):
        user_pass = data_in.get("password")
        if user_pass:
            data_in["password"] = get_hash(user_pass)
        return self.user_dao.update(data_in)

    def delete(self, uid):
        return self.user_dao.delete(uid)
