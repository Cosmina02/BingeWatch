import json
from requests import get


def get_tv_show_id(show_title):
    url = r"https://api.tvmaze.com/search/shows?q="
    show_title.replace("'", "+")
    show_title.replace(" ", "+")
    url = url + show_title
    response = get(url)
    json_data = json.loads(response.text)
    for data in json_data:
        return data["show"]["id"]


def get_show_episode(show_title):
    id = get_tv_show_id(show_title)
    url = r"https://api.tvmaze.com/shows/" + str(id) + "/episodes"
    response = get(url)
    json_data = json.loads(response.text)
    episode_dict = dict()
    episode_list = list()
    season = 1
    for data in json_data:
        print(f"season {data['season']} , number  { data['number']}")
        if season == data['season']:
            episode_list.append(data['number'])
        else:
            episode_dict[season] = episode_list
            season = data['season']
            episode_list = list()
            episode_list.append(data['number'])
    episode_dict[season] = episode_list
    return episode_dict


if __name__ == '__main__':
    show_title = "Grey's Anatomy"
    episodes = get_show_episode(show_title)
    for key,value in episodes.items():
        print(f"season:{key}, episodes{value}")

