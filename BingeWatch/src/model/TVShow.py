from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TvShow(Base):
    __tablename__ = 'tvshows'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String, nullable=False)
    link = Column("link", String, nullable=False)
    last_episode = Column("last_episode", String)
    last_date = Column("last_date", Date)
    score = Column("score", Integer)
    snoozed = Column("snoozed", Boolean, default=False)

    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.last_episode = None
        self.last_date = None
        self.score = None

    def set_last_episode(self, last_episode):
        self.last_episode = last_episode

    def set_last_date(self,last_date):
        self.last_date = last_date

    def set_score(self, score):
        self.score = score

