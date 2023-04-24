import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
from sqlalchemy import orm



class TypeUsers(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'type_users'

    id_type_user = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_user = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id_user'))
    user = orm.relationship("User", back_populates='type_u')
    id_type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('types.id_type'))
    types = orm.relationship("Types", back_populates='types')
