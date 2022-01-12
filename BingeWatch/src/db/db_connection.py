from sqlalchemy import create_engine
from src.db.db_settings import postgresql


class Database:
    """
    A class which handles the database connection


    Attributes
    ----------
    connection : Database
                the database connection itself

    engine : Engine
           It is an instance of the Engine class that provides connectivity to the database

    Methods
    -------
    get_instance()
        Returns the instance of the database class.
    """
    connection = None

    @staticmethod
    def get_instance():
        """
        Returns the instance of the database class.
        It is used to preserve the singleton so we don't have multiple instances of the database.

        :return: an instance of the database class
        """
        if Database.connection is None:
            Database()
        return Database.connection

    def __init__(self):
        """
        Private constructor. Creates the database connection.
        All the parameters that are necessary to connect to the database are from the db_settings.py file.
        """
        if Database.connection is not None:
            raise Exception("You are trying to create multiple instances of a singleton")
        else:
            Database.connection = self
            url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
                user=postgresql['pguser'], passwd=postgresql['pgpasswd'], host=postgresql['pghost'],
                port=postgresql['pgport'], db=postgresql['pgdb'])
            try:
                self.engine = create_engine(url, pool_size=50)
                print("Connected to PostgreSQL database!")
            except IOError:
                print("Failed to connect to the database.")
