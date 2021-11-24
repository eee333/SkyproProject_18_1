# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from marshmallow import fields, Schema
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_filter(self, filter_dict):
        return self.session.query(Movie).filter_by(**filter_dict).all()

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

    def create(self, data_in):
        obj = Movie(**data_in)
        self.session.add(obj)
        self.session.commit()
        return obj

    def update(self, data_in):
        obj = self.get_one(data_in.get('id'))
        if obj:
            if data_in.get('title'):
                obj.title = data_in.get('title')
            if data_in.get('description'):
                obj.description = data_in.get('description')
            if data_in.get('trailer'):
                obj.trailer = data_in.get('trailer')
            if data_in.get('year'):
                obj.year = data_in.get('year')
            if data_in.get('rating'):
                obj.rating = data_in.get('rating')
            if data_in.get('genre_id'):
                obj.genre_id = data_in.get('genre_id')
            if data_in.get('director_id'):
                obj.director_id = data_in.get('director_id')
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


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
