'''web crawler to extract lyrics from the web.
im thinking i just need to pout bs in the right direction and then send it out.
az format is like https://www.azlyrics.com/'first letter of artist'/'artistname'.html
'''

from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as ss
import time
import re
import urllib.request as ur
import requests

proxies = {'https': '93.80.26.110'}

azUrl = "https://www.azlyrics.com/"
#chance = "https://www.azlyrics.com/c/chancetherapper.html"
dots = '..'
#testList = ["chancetherapper", "kyle", "kidsseeghost", "dirty heads"]

def getArtistUrl(artist):
    artist = artist.lower()
    artist = artist.replace(" ","")
    artistUrl = azUrl + artist[0] + "/" + artist + ".html"
    return artistUrl

def getLyrics(artist):
    artistUrl = getArtistUrl(artist)
    result = requests.get(artistUrl)
    soup = bs(result.content, "html.parser")
    for thing in soup.find_all(target="_blank"):
        stringThing = str(thing['href'])
        #print(stringThing)
        if stringThing.startswith(dots) > 0:
            url = azUrl + stringThing[3:]
            #print(url)
            songUrl = requests.get(url)
        else:
            #print("false")
            #print(thing['href'])
            songUrl = requests.get(thing['href'])
        #print(songUrl)
        time.sleep(2.5)
        songSoup = bs(songUrl.content, "html.parser")
        #print(songSoup.find_all_next(class_= "col-xs-12 col-lg-8 text-center"))
        base = songSoup.find(class_ = "ringtone")
        lyrics = base.find_next_sibling("div")
        print(lyrics.get_text())

#getLyrics("taylorswift")