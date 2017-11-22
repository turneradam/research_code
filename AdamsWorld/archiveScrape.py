import json
import requests
import time
import traceback

SEARCH_ROOT = "https://gifcities.archive.org/api/v1/gifsearch?q=%s&seed=1000"
DOWNLOAD_ROOT = "https://web.archive.org/web/"
TARGET_DIR = "./gifs2/"
Alphabet = "qwertyuiopasdfghjklzxcvbnm"
words = ""

def getList(search_term):
    raw_content = requests.get(SEARCH_ROOT % search_term)
    json_list = json.loads(raw_content.content)
    return json_list

def make_pull_and_save(url):
    try:
        img_data = requests.get(url)
        _name = url.split("/")[-1]
        resp = requests.get(url)

        with open(TARGET_DIR + _name, "wb") as sav_fil:
            sav_fil.write(resp.content)

        return True

    except:
        traceback.print_exc()
        raw_input()
        return False


def run(_array = Alphabet):
    for i in _array:
        for dic_struct in getList(i):
            suffix = dic_struct["gif"]    
            search_url = DOWNLOAD_ROOT + suffix
            if make_pull_and_save(search_url):
                print "GOT" + suffix

            else:
                print "ERROR on " + suffix



run()
