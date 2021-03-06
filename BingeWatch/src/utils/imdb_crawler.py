import requests
import re


def find_imdb_link(show_title):
    """
        Method that crawls the imdb search page and gets the identification number
    for a certain show and constructs it's imdb link.
    :param show_title: str (the show of the title)
    :return: the imdb link for the show given as a parameter
    """
    site = r"https://www.imdb.com/find?q="
    site_end = "&ref_=nv_sr_sm"
    show_title.lower()
    show_title = show_title.replace("'", "+")
    show_title = show_title.replace(" ", "+")
    site = site + show_title + site_end

    r = requests.get(site)
    r.raise_for_status()

    html_content = r.text
    tv_show_link = re.findall('<a href="/title/[a-z]*[0-9]*/"', html_content)

    imdb_link = r"https://www.imdb.com" + tv_show_link[0][9:-1] + "?ref_=fn_al_tt_1"

    return imdb_link
