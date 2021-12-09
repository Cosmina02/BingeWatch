from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util.compat import contextmanager

from src.db.db_connection import *

@contextmanager
def session_scope():
    connection = Database.get_instance()
    engine = connection.engine
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
        session.commit()
    except exc.SQLAlchemyError:
        session.rollback()
        print("SQLAlchemy Error-could not create session-rollback done")
    finally:
        session.close()
        print("Session Closed!")