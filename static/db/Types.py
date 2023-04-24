import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Types(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'types'

    id_type = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title_type = sqlalchemy.Column(sqlalchemy.String(20), unique=True, nullable=True)
    # types = orm.relationship('TypeUsers')