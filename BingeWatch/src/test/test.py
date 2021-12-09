from src.model.TVShow import TvShow
from sqlalchemy import exc


class Test:

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

    def get_all_shows(self):
        return self.session.query(TvShow).all()


