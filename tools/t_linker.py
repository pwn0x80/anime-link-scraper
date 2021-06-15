#!/usr/bin/python3
import requests
import sys
from bs4 import *

def t_link(url):
    resp = requests.get(url)
    text_resp = resp.text
    soup = BeautifulSoup(text_resp, "lxml")
    soup_link = soup.find_all('a')
    l_link = [i.get('href') for i in soup_link]
    return(l_link)
