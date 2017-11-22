import requests 
import os
import traceback

RANGE_1 = 100
RANGE_2 = 100

FRAME = "http://www.cameronsworld.net/img/content/%s/%s.gif"



def tryGrab(endpoint):
    print "Trying: %s" % endpoint
    try:
        resp = requests.get(endpoint)
        if resp.status_code != 200: 
            raise Exception("No image")
        return resp
    except:
        traceback.print_exc()
        return False


for x in range(RANGE_1):
    for y in range(RANGE_2):
        resp = tryGrab(FRAME % (x,y))
        if resp:
            with open ("gifs/%s_%s.gif" % (x,y),"wb") as fil:
                print "Writing %s_%s.gif" % (x,y)
                fil.write(resp.content)
                

