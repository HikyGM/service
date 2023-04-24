import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()
__factory = None


def global_init():
    global __factory
    if __factory:
        return
    conn_str = 'postgresql+psycopg2://postgres:123@localhost:5432/service_api'
    engine = sa.create_engine(conn_str)
    __factory = orm.sessionmaker(bind=engine)
    # noinspection PyUnresolvedReferences
    from . import __all_models__
    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
