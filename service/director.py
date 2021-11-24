# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.


class DirectorService:

    def __init__(self, director_dao):
        self.director_dao = director_dao

    def get_all(self):
        return self.director_dao.get_all()

    def get_one(self, uid):
        return self.director_dao.get_one(uid)

    def create(self, data_in):
        return self.director_dao.create(data_in)

    def update(self, data_in):
        return self.director_dao.update(data_in)

    def delete(self, uid):
        return self.director_dao.delete(uid)
