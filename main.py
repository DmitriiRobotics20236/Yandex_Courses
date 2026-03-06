from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    db_sess = db_session.create_session()

    captain = User(
        surname='Scott',
        name='Ridley',
        age=21,
        position='captain',
        speciality='research engineer',
        address='module_1',
        email='scott_chief@mars.org'
    )
    db_sess.add(captain)

    colonist1 = User(
        surname='Doe',
        name='John',
        age=30,
        position='pilot',
        speciality='engineer',
        address='module_2',
        email='john_doe@mars.org'
    )
    db_sess.add(colonist1)

    colonist2 = User(
        surname='Smith',
        name='Jane',
        age=28,
        position='doctor',
        speciality='medical',
        address='module_3',
        email='jane_smith@mars.org'
    )
    db_sess.add(colonist2)

    colonist3 = User(
        surname='Williams',
        name='Mark',
        age=25,
        position='biologist',
        speciality='ecological researcher',
        address='module_4',
        email='mark_williams@mars.org'
    )
    db_sess.add(colonist3)

    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
