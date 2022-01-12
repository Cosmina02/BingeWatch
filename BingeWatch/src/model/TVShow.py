from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TvShow(Base):
    """
    Class that represents the a tv show.

    Attributes
    ----------
    id : int
        the id of the tv show in the database
    title : str
        the title of the tv show
    link : str
        link to the tv show's imdb page
    last_season : int
        the season the user is currently watching
    last_episode : int
        the last watched episode
    last_date : date
        the date when the last episode was seen
    score : int
        the user score for the tv show
    snoozed : bool
        true if a show is snoozed,false otherwise

    Methods
    -------
    set_last_episode(last_episode, last_season):
        sets the last watched episode and season
    set_last_date(last_date):
        sets the last watched date
    set_score(self, score):
        sets the score
    """

    __tablename__ = 'tvshows'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String, nullable=False)
    link = Column("link", String, nullable=False)
    last_season = Column("last_season", Integer)
    last_episode = Column("last_episode", Integer)
    last_date = Column("last_date", Date)
    score = Column("score", Integer)
    snoozed = Column("snoozed", Boolean, default=False)

    def __init__(self, title):
        self.title = title
        self.link = None
        self.last_season = None
        self.last_episode = None
        self.last_date = None
        self.score = None

    def set_last_episode(self, last_episode, last_season):
        """
        Sets the last watched episode and season
        :param last_episode: int
        :param last_season: int
        :return: None
        """
        self.last_episode = last_episode
        self.last_season = last_season

    def set_last_date(self, last_date):
        """
        Sets the last watched date
        :param last_date: Date
        :return: None
        """
        self.last_date = last_date

    def set_score(self, score):
        """
        Sets the score
        :param score: int
        :return: None
        """
        self.score = score
