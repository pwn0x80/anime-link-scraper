#!/usr/bin/python3
import requests
import sys
import os
from bs4 import *
import tools.id_finder
import tools.t_linker

os.system("clear")

print("\t" + "#" * 80 + "#")
print(
    "\t" + "#\033[91m\t[*] \t\t\t\tpwn0x80\033[0m\t\t\t\t\t" + "#")

print(
    "\t" + "#\033[91m\t[*] WeBsiTe - pwn0x80.github.io\033[0m\t\t\t\t\t\t" + "#")
print(
    "\t" + "#\033[91m\t[*] https://github.com/aditya0x80\033[0m\t\t\t\t\t" + "#")

print(
    "\t" + "#\033[91m\t[*] https://www.instagram.com/pwn0x80/\033[0m\t\t\t\t\t" + "#")
print("\t" + "#" * 80 + "#")
print("")

current_dir = os.getcwd()  # current dir

# link
link = sys.argv[1]
linksplit = link.split("/")  # split link


# remove file
try:
    os.remove(current_dir+"/anime_link/{}.txt".format(linksplit[4]))
except OSError:
    pass

# url
URL_patten_ep = "https://www1.gogoanime.ai{}"
url_patten_id = "https://www1.gogoanime.ai/category/{}"
url_patten_sep = "https://ajax.gogo-load.com/ajax/load-list-episode?ep_start=0&ep_end=1900&id={}"
text_file = "anime_link/{}.txt"

# id finder
url_id = url_patten_id.format(linksplit[4])
anime_id = tools.id_finder.id_find(url_id)

# eps links
url_sep = url_patten_sep.format(anime_id)
anime_sep = tools.t_linker.t_link(url_sep)
anime_sep.reverse()
for i in anime_sep:
    i = i.strip()
    url = URL_patten_ep.format(i)

# parser
    resp = requests.get(url)
    text_resp = resp.text     # website source code
    soup = BeautifulSoup(text_resp, "lxml")
    soup_ep = soup.find('a', {'class': 'active'})
    link = soup_ep.get('data-video')

# save at text file
    f = open(text_file.format(linksplit[4]), "a")
    f.write("https:"+link+"\n\n")
    print("wait...")
print("done!!!")
