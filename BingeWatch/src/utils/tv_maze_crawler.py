import json
from requests import get


def get_tv_show_id(show_title):
    """
        Methods that gets the show's id. It makes a request on the tv maze api and gets the id.
    :param show_title: str (the show title we need the id)
    :return:
    """
    url = r"https://api.tvmaze.com/search/shows?q="
    show_title.replace("'", "+")
    show_title.replace(" ", "+")
    url = url + show_title
    response = get(url)
    json_data = json.loads(response.text)
    for data in json_data:
        return data["show"]["id"]


def get_show_episode(show_title):
    """
        Method that makes a request on the tv maze api and retrieves all the seasons and
    episodes of the requested tv show.
    :param show_title: str ( the show title we want to get all the episodes)
    :return: a dictionary with all the seasons and episodes of the tv show
    """
    show_id = get_tv_show_id(show_title)
    url = r"https://api.tvmaze.com/shows/" + str(show_id) + "/episodes"
    response = get(url)
    json_data = json.loads(response.text)
    episode_dict = dict()
    episode_list = list()
    season = 1
    for data in json_data:
        if season == data['season']:
            episode_list.append(data['number'])
        else:
            episode_dict[season] = episode_list
            season = data['season']
            episode_list = list()
            episode_list.append(data['number'])
    episode_dict[season] = episode_list
    return episode_dict
