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
from lyrics import lyrics
from itertools import cycle

proxies = {'https': '93.80.26.110'}

azUrl = "https://www.azlyrics.com/"
#chance = "https://www.azlyrics.com/c/chancetherapper.html"
dots = '..'
#testList = ["chancetherapper", "kyle", "kidsseeghost", "dirty heads"]


proxies = ['192.69.245.61', '47.89.241.103	', '198.50.187.74']
proxyCycle = cycle(proxies)


def getArtistUrl(artist):
    temp = artist.lower()
    temp = temp.replace(" ","")
    artistUrl = azUrl + temp[0] + "/" + temp + ".html"
    return artistUrl

def getLyrics(artist,lyric):
    artistUrl = getArtistUrl(artist)
    result = requests.get(artistUrl)
    soup = bs(result.content, "html.parser")

    for thing in soup.find_all(target="_blank"):
        proxy = next(proxyCycle)
        stringThing = str(thing['href'])
        #print(stringThing)
        if stringThing.startswith(dots) > 0:
            url = azUrl + stringThing[3:]
            #print(url)
            try:
                songUrl = requests.get(url, proxies={"http":proxy, "https":proxy})
                print("used proxy")
            except:
                songUrl = requests.get(url)
                print("no proxy")
        else:
            #print("false")
            #print(thing['href'])
            try:
                songUrl = requests.get(thing['href'], proxies={"http":proxy, "https":proxy})
                print("proxy")
            except:
                songUrl = requests.get(thing['href'])
                print("no proxy")

        #print(songUrl)
        time.sleep(7)
        songSoup = bs(songUrl.content, "html.parser")
        #print(songSoup.find_all_next(class_= "col-xs-12 col-lg-8 text-center"))
        base = songSoup.find(class_ = "ringtone")
        lyrics = base.find_next_sibling("div")
        artist_name = songSoup.find_all('b')
        new_name = str(artist_name[2])
        alb_name = new_name.split('"')
        #print(alb_name[1])
        #print(lyrics.get_text())
        print("Obtained lyrics")
        song_name = songSoup.find_all('script')
        song_name1 = str(song_name[0])
        song_name2 = song_name1.split('\n')
        song_name3 = song_name2[2].split('"')
        #print(song_name3[1])
        lyric.add_song(artist,alb_name[1],song_name3[1],str(lyrics.get_text()))
    return lyric   #FOR CASEY I put the return in the loop to kill the function early to prevent blacklisting while testing

test = lyrics()
plz = getLyrics("KIDS SEE GHOSTS",test)
print("So there where: ", len(plz.get_words_artist("KIDS SEE GHOSTS")), "WORDS!!!!!")
print(test.artists)

