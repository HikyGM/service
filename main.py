from flask import Flask, render_template
import static.db.db_session as db_session
app = Flask(__name__)
'''
        Для создания комита изменения базы
        alembic revision --autogenerate -m "добавили признак публикации"

        Обновить базу
        alembic upgrade head

        Откатиться к предыдушей версии
        alembic downgrade head

        head означает, что мы хотим применить все миграции 
        друг за другом для приведения базы в самое актуальное 
        состояние. Вместо head можно указать номер ревизии
        или написать, например, +2, 
        чтобы обновиться только на 2 следующие версии.
'''

def main():
    db_session.global_init()
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
