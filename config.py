# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

# Пример

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/movie.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
