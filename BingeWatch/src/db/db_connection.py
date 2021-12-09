from sqlalchemy import create_engine
from src.db.db_settings import postgresql


class Database:
    connection = None

    @staticmethod
    def get_instance():
        if Database.connection is None:
            Database()
        return Database.connection

    def __init__(self):
        if Database.connection is not None:
            raise Exception("You are trying to create multiple instances of a singleton")
        else:
            Database.connection = self
            url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
                user=postgresql['pguser'], passwd=postgresql['pgpasswd'], host=postgresql['pghost'], port=postgresql['pgport'], db=postgresql['pgdb'])
            try:
                self.engine = create_engine(url, pool_size=50)
                print("Connected to PostgreSQL database!")
            except IOError:
                print("Failed to connect to the database.")
