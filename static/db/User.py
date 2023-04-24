import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'

    id_user = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email_user = sqlalchemy.Column(sqlalchemy.String(50), index=True, unique=True, nullable=True)
    login_user = sqlalchemy.Column(sqlalchemy.String(50), nullable=True, unique=True)  # unique=True,
    password_user = sqlalchemy.Column(sqlalchemy.String(256), nullable=True)
    first_name_user = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
    last_name_user = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
    patronymic_user = sqlalchemy.Column(sqlalchemy.String(50))
    day_of_birth = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    gender_user = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    path_im_user = sqlalchemy.Column(sqlalchemy.String(50), nullable=True, default='static/images/nonePhoto.png')
    phone_number = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
    type_u = orm.relationship('TypeUsers')
    group_u = orm.relationship('GroupsUsers')

    def set_password(self, password):
        self.password_user = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_user, password)
