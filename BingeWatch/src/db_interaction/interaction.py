from src.model.TVShow import TvShow
from sqlalchemy import exc, func


# class which handles the database interaction(query-> model)

class Interaction:

    def __init__(self, session):
        self.session = session

    def insert_show(self, tv_show: TvShow):
        try:
            self.session.add(tv_show)
            self.session.commit()
            print(f'Show added successfully.')
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Could not add show. Rollback done.")

    def delete_show(self, show_title):
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).delete(synchronize_session=False)
            self.session.commit()
            print("Show deleted successfully")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Could not delete the show.Rollback done!")

    def get_all_shows(self):
        return self.session.query(TvShow).all()

    def update_last_watched_episode(self, show_title, season, episode):
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).update({
                TvShow.last_season: season}, synchronize_session=False)
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).update({
                TvShow.last_episode: episode}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def update_last_watched_date(self, show_title, date):
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).update({
                TvShow.last_date: date}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def update_score(self, show_title, score):
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).update({
                TvShow.score: score}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def snooze_tv_show(self, show_title):
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).update({
                TvShow.snoozed: True}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def unsnooze_tv_show(self, show_title):
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).update({
                TvShow.snoozed: False}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")
