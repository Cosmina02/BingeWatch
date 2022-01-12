from src.model.TVShow import TvShow
from src.utils.youtube_crawler import get_youtube_uploads
from datetime import datetime, date
from src.utils.tv_maze_crawler import get_show_episode


def add_tvShow(repo):
    """
        Calls the insert_show method from the Interaction class
    :param repo: an instance of the Interaction class
    :return: None
    """
    show_title = input("Please enter the name of the TvShow you want to add: ")
    if not repo.is_show_in_db(show_title):
        repo.insert_show(TvShow(show_title))
    else:
        print("The show you just enter is already in the database.")


def delete_tvShow(repo):
    """
        Calls the delete_show method from the Interaction class
    :param repo: an instance of the Interaction class
    :return: None
    """
    show_title = input("Please enter the name of the TvShow you want to delete: ")
    if not repo.is_show_in_db(show_title):
        print("You are trying to delete a show that doesn't exist!")
    else:
        repo.delete_show(show_title)


def modify_score(repo):
    """
        Calls the update_score method from the Interaction class
    :param repo: an instance of the Interaction class
    :return: None
    """
    show_title = input("Please enter the name of the TvShow for which you want to modify the score: ")
    if not repo.is_show_in_db(show_title):
        print("The show you entered doesn't exist. Press 1 if you want to add it in you database.")
    else:
        score = input("Please enter the score: ")
        while int(score) < 0 or int(score) > 10:
            score = input("Please enter a valid score(between 0 and 10): ")
        repo.update_score(show_title, score)


def snooze(repo):
    """
        Calls the snooze_tv_show method from the Interaction class
    :param repo:an instance of the Interaction class
    :return: None
    """
    show_title = input("Please enter the name of the TvShow you want to snooze: ")
    if not repo.is_show_in_db(show_title):
        print("The show you entered doesn't exist. Press 1 if you want to add it in you database.")
    else:
        repo.snooze_tv_show(show_title)


def unsnooze(repo):
    """
        Calls the unsnooze_tv_show method from the Interaction class
    :param repo: an instance of the Interaction class
    :return: None
    """
    show_title = input("Please enter the name of the TvShow you want to unsnooze: ")
    if not repo.is_show_in_db(show_title):
        print("The show you entered doesn't exist. Press 1 if you want to add it in you database.")
    else:
        repo.unsnooze_tv_show(show_title)


def see_youtube_uploads(repo):
    """
        Displays the youtube uploads for a tv show. If the user wants to see uploads about the last
    watched episode it can choose to.
    :param repo: an instance of the Interaction class
    :return: None
    """
    show_title = input("Please enter the name of the TvShow want to see youtube uploads about: ")
    decision = input("Do you want to see uploads about the last episode you watched?y/n ")

    if decision == 'y':
        last_watched_episode = repo.get_last_seen_episode(show_title)
        search_words = show_title + " " + last_watched_episode
        videos = get_youtube_uploads(search_words)
    else:
        videos = get_youtube_uploads(show_title)
    for video in videos:
        print("https://www.youtube.com/watch?v="+video)


def update_episode(repo):
    """
        Updates the last watched episode by calling the update_last_episode method from the interaction class.
    The user can say if they started a new season or not,if they didn't the season will not be changed.
    :param repo: an instance of the Interaction class
    :return: None
    """
    show_title = input("Please enter the name of the TvShow you want to update the episode: ")
    if not repo.is_show_in_db(show_title):
        print("The show you entered doesn't exist. Press 1 if you want to add it in you database.")
    else:
        decision = input("Did you start a new season? y/n ")
        if decision == 'y':
            season = input("Please enter the number of the season you are currently watching: ")
            while int(season) < 1:
                season = input("Please enter a valid season number(the number cannot be less than 1): ")
        else:
            season = None
        episode = input("Please enter the number of the last episode you watched: ")
        while int(episode) < 1:
            episode = input("Please enter a valid episode number(greater than 0): ")
        repo.update_last_watched_episode(show_title, episode, season)
        today = date.today()
        repo.update_last_watched_date(show_title, today)


def update_last_watched_date(repo):
    """
        Updates the last watched date for an episode. If an user doesn't update it will be automatically
    updated when the last episode is updated.
    :param repo: an instance of the Interaction class
    :return: None
    """
    show_title = input("Please enter the name of the TvShow")
    if not repo.is_show_in_db(show_title):
        print("The show you entered doesn't exist. Press 1 if you want to add it in you database.")
    else:
        data = input("Please enter the date! The format is YYYY-MM-DD : ")
        try:
            datetime.strptime(data, '%Y-%m-%d')
            repo.update_last_watched_date(show_title, data)
        except ValueError:
            # raise Exception("Invalid date input! The date should be YYYY-MM-DD")
            print("Invalid date input! The date should be YYYY-MM-DD")


def list_new_episodes(repo):
    """
        Displays all the new episodes for all the shows that are not snoozed.
    :param repo: an instance of the Interaction class
    :return: None
    """
    print("Listing may take a few seconds... Please wait patiently\n")
    shows = repo.get_all_unsnoozed_shows()
    for show in shows:
        all_episodes = get_show_episode(show.title)
        episode = show.last_episode
        season = show.last_season
        if episode is None or season is None:
            print(f"Looks like you haven't started watching {show.title}")
            print("Here you have the list of all the episodes and seasons for this show: ")
            for key, value in all_episodes.items():
                print(f"season:{key}, episodes{value}")
        else:
            print(f"Here are the new episodes for {show.title}")
            for key, value in all_episodes.items():
                if key == season:
                    i = value.index(episode)
                    remaining_episodes = list()
                    for v in range(i+1, len(value)):
                        remaining_episodes.append(v)
                    print(f"season:{key}, episodes:{remaining_episodes}")
                elif key > season:
                    print(f"season:{key}, episodes: {value}")
            print("\n")


def list_all_shows(repo):
    """
        Displays all the shows.
    :param repo: an instance of the Interaction class
    :return: None
    """
    shows = repo.get_all_shows()
    for show in shows:
        print(show.title)


def pick_command(repo):
    """
        Command line method. Displays all the commands and lets the user choose.
    :param repo: an instance of the Interaction class
    :return: None
    """
    print("Hello! Welcome to BingeWatch!\n "
          "You can choose from the following commands:\n"
          "1.Add a TvShow\n"
          "2.Delete a TvShow\n"
          "3.Modify the score\n"
          "4.Snooze\n"
          "5.Unsnooze\n"
          "6.List new episodes\n"
          "7.See youtube uploads\n"
          "8.Update last seen episode\n"
          "9.Update last seen at this date\n"
          "10.List all shows\n"
          "11.Help\n"
          "12.Exit\n")
    command = input("Please pick one number: ")
    while command != '12':
        if command == '1':
            print("Add a TvShow")
            add_tvShow(repo)
        elif command == '2':
            print("Delete a TvShow")
            delete_tvShow(repo)
        elif command == '3':
            print("Modify the score")
            modify_score(repo)
        elif command == '4':
            print("Snooze")
            snooze(repo)
        elif command == '5':
            print("Unsnooze")
            unsnooze(repo)
        elif command == '6':
            print("List new episodes")
            list_new_episodes(repo)
        elif command == '7':
            print("See youtube uploads")
            see_youtube_uploads(repo)
        elif command == '8':
            print("Update last seen episode")
            update_episode(repo)
        elif command == '9':
            print("Update last seen at this date")
            update_last_watched_date(repo)
        elif command == '10':
            print("Listing all the shows")
            list_all_shows(repo)
        elif command == '11':
            print("Hello! You can choose from the following commands:\n"
                  "1.Add a TvShow\n"
                  "2.Delete a TvShow\n"
                  "3.Modify the score\n"
                  "4.Snooze\n"
                  "5.Unsnooze\n"
                  "6.List new episodes\n"
                  "7.See youtube uploads\n"
                  "8.Update last seen episode\n"
                  "9.Update last seen at this date\n"
                  "10.List all shows\n"
                  "11.Help\n"
                  "12.Exit\n")
        else:
            print("Unknown command! Try again!")
        command = input("Please pick one number:\nIf you forgot the commands please enter 11 to see them all:  ")
