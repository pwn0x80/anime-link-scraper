#!/usr/bin/python3
import requests
import sys
from bs4 import *

def id_find(url):
    resp = requests.get(url)
    text_resp = resp.text
    soup = BeautifulSoup(text_resp, "lxml")
    soup_ep = soup.find('div', {'class': 'anime_info_episodes_next'}).find(
        "input").get("value")
    return(soup_ep)
