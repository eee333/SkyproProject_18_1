# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.


class MovieService:

    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_all(self):
        return self.movie_dao.get_all()

    def get_filter(self, filter_dict):
        filter_dict_clear = {}
        for key, value in filter_dict.items():
            if value is not None:
                filter_dict_clear[key] = value
        return self.movie_dao.get_filter(filter_dict_clear)

    def get_one(self, uid):
        return self.movie_dao.get_one(uid)

    def create(self, data_in):
        return self.movie_dao.create(data_in)

    def update(self, data_in):
        return self.movie_dao.update(data_in)

    def delete(self, uid):
        return self.movie_dao.delete(uid)
