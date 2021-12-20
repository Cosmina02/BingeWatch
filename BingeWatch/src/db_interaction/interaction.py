from src.model.TVShow import TvShow
from sqlalchemy import exc, func
from src.utils.imdb_crawler import find_imdb_link


# class which handles the database interaction(query-> model)

class Interaction:

    def __init__(self, session):
        self.session = session

    def insert_show(self, tv_show: TvShow):
        tv_show.link = find_imdb_link(tv_show.title)
        try:
            self.session.add(tv_show)
            self.session.commit()
            print(f'Show added successfully.')
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Could not add show. Rollback done.")

    def delete_show(self, show_title):
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()). \
                delete(synchronize_session=False)
            self.session.commit()
            print("Show deleted successfully")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Could not delete the show.Rollback done!")

    def get_all_shows(self):
        return self.session.query(TvShow).all()

    def update_last_watched_episode(self, show_title, episode, season=None):
        try:
            if season is None:
                self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).update({
                    TvShow.last_episode: episode}, synchronize_session=False)
            else:
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

    def get_last_seen_episode(self, show_title):
        show_info = self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).one()
        if show_info.last_season is None and show_info.last_episode is None:
            return "Looks like you haven't started the show yet!"
        else:
            last_seen_episode = "season " + str(show_info.last_season) + " episode " + str(show_info.last_episode)
            return last_seen_episode
