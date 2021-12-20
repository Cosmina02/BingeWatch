import requests
import re


def get_youtube_uploads(search_words):
    site = r"https://www.youtube.com/results?search_query="
    search_words.replace("'", "+")
    search_words.replace(" ", "+")
    site = site + search_words

    r = requests.get(site)
    r.raise_for_status()

    html_content = r.text
    video_ids = re.findall(r"watch\?v=(\S{11})", html_content)

    return video_ids


