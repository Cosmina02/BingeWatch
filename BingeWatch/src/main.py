from src.db.session import session_scope
from src.db_interaction.interaction import *
from src.model.TVShow import*


if __name__ == '__main__':

    with session_scope() as crt_session:
        repo = Interaction(crt_session)
        # show = TvShow("Suits", f"https://www.imdb.com/title/tt1632701/?ref_=fn_al_tt_1")
        # repo.insert_show(show)
        # repo.insert_show(TvShow(f"Grey's Anatomy"))
        # repo.insert_show(TvShow(f"The Mentalist", f"https://www.imdb.com/title/tt1196946/?ref_=nv_sr_srsg_0"))

        # repo.delete_show(f"Grey's Anatomy")
        shows = repo.get_all_shows()
        for show in shows:
            print(show.title, " ", show.link, " ", show.last_season, " ", show.last_episode, " ",
                  show.last_date, " ", show.score, " ", show.snoozed)

        print(repo.get_last_seen_episode("The Mentalist"))

        # repo.update_last_watched_episode("Suits", 1, 2)
        # repo.update_last_watched_date("Suits", f"2021-11-03")

        # repo.update_score("The Mentalist", 6)
        #
        # repo.snooze_tv_show("Grey's Anatomy")




