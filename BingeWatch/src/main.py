from src.db.session import session_scope
from src.test.test import *
from src.model.TVShow import*


if __name__ == '__main__':

    with session_scope() as crt_session:
        test = Test(crt_session)
        show = TvShow("you", f"https://www.imdb.com/title/tt0413573/?ref_=fn_al_tt_1")
        test.insert_show(show)
        test.insert_show(TvShow(f"How to get away with murder", f"https://www.imdb.com/title/tt3205802/?ref_=fn_al_tt_1"))
        shows = test.get_all_shows()
        print(shows)

