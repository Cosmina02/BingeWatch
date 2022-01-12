from src.model.TVShow import TvShow
from sqlalchemy import exc, func
from src.utils.imdb_crawler import find_imdb_link


class Interaction:
    """
    A class to represent the database interaction.

    ...
    Attributes
    ----------
    session:
        database session on which all the queries will take place

    Methods
    -------
    insert_show(tv_show):
        Adds a new tv show to the database.
    delete_show(show_title):
        Deletes a tv show from the database.
    get_all_shows():
        Returns a list of all the tv shows from the database.
    get_all_usnoozed_shows():
        Returns a list of all the shows that are not snoozed from the database.
    update_last_watched_episode(show_title, episode, season):
        Updates the last watched episode for a certain tv show.
    update_last_watched_date(show_title, date):
        Updates the last watched date for a certain tv show.
    update_score(show_title, score):
        Updates the score for a certain tv show.
    snooze_tv_show(show_title):
        Sets the show on snooze.
    unsnooze_tv_show(show_title):
        Sets the show on unsnooze.
    get_last_seen_episode(show_title):
        Returns the last seen episode for a certain show.
    is_show_in_db(show_title):
        Returns a boolean value if the show is in the database or not.
    """

    def __init__(self, session):
        """
        Constructor.
        :param session:
            database session on which all the queries will take place
        """
        self.session = session

    def insert_show(self, tv_show: TvShow):
        """
        Adds a new tv show to the database.
        :param tv_show: a tv show object that will be added to the database
        :return: None
        """
        tv_show.link = find_imdb_link(tv_show.title)
        try:
            self.session.add(tv_show)
            self.session.commit()
            print(f'Show added successfully.')
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Could not add show. Rollback done.")

    def delete_show(self, show_title):
        """
        Deletes a tv show from the database.
        :param show_title: the name of the show that is going to be deleted
        :return: None
        """
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()). \
                delete(synchronize_session=False)
            self.session.commit()
            print("Show deleted successfully")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Could not delete the show.Rollback done!")

    def get_all_shows(self):
        """
        :return: a list of all the shows found in the database
        """
        return self.session.query(TvShow).all()

    def get_all_unsnoozed_shows(self):
        """
        :return: a list of all the shows that are not snoozed
        """
        return self.session.query(TvShow).filter(TvShow.snoozed == 'False').all()

    def update_last_watched_episode(self, show_title, episode, season=None):
        """
        Updates the last watched episode for a certain tv show.
        :param show_title: the title of the tv show that is going to be updated
        :param episode: the number of the episode
        :param season: the number of the season
        :return: None
        """
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
        """
         Updates the last watched date for a certain tv show.
        :param show_title: the title of the tv show that is going to be updated
        :param date: the last watched date
        :return: None
        """
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).update({
                TvShow.last_date: date}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def update_score(self, show_title, score):
        """
        Updates the score for a certain tv show.
        :param show_title: the title of the tv show that is going to be updated
        :param score: the score number
        :return: None
        """
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).update({
                TvShow.score: score}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def snooze_tv_show(self, show_title):
        """
        Sets the show on snooze.
        :param show_title: the title of the tv show that is going to be snoozed
        :return: None
        """
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).update({
                TvShow.snoozed: True}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def unsnooze_tv_show(self, show_title):
        """
        Sets the show on unsnooze.
        :param show_title: the title of the tv show that is going to be unsnoozed
        :return: None
        """
        try:
            self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).update({
                TvShow.snoozed: False}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def get_last_seen_episode(self, show_title):
        """
        :param show_title: the title of the tv show
        :return: the last seen episode of the given tv show
        """
        show_info = self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).one()
        if show_info.last_season is None and show_info.last_episode is None:
            return "Looks like you haven't started the show yet!"
        else:
            last_seen_episode = "season " + str(show_info.last_season) + " episode " + str(show_info.last_episode)
            return last_seen_episode

    def is_show_in_db(self, show_title):
        """
        :param show_title: the title of the tv show
        :return: a boolean value if the show is in the database or not
        """
        return self.session.query(TvShow).filter(func.lower(TvShow.title) == show_title.lower()).scalar() is not None
