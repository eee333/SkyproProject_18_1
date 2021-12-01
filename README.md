Фильмотека
=======
API приложение для доступа к базе фильмов. 
------------
1. Доступ открыт только для зарегистрированных пользователей.
2. Удалять и редактировать может только администратор.
3. Фильмы можно фильтровать по режисерам, жанрам и году ввхода на экран.

Примеры запросов:
-------------
GET
* http://localhost:10001/movies/
* http://localhost:10001/movies/21
* http://localhost:10001/directors/
* http://localhost:10001/directors/3
* http://localhost:10001/genres/
* http://localhost:10001/genres/18
* http://localhost:10001/users/
* http://localhost:10001/users/2

Пользователи:
------
1. (username="vasya", password="my_little_pony", role="user")
2. (username="oleg", password="qwerty", role="user")
3. (username="boss", password="P@ssw0rd", role="admin")
4. (username="eee", password="1234", role="user")

Пароли пользователей хешируются.
Доступ через токены.
