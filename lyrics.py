import json
import re
class lyrics:

    def __init__(self):
        self.artists = {}
        self.notword = "\n\r\"\'"
        self.search = {}
        try:
            with open("search") as f:
                self.search = json.load(f)
        except FileNotFoundError:
            pass

    def search_artist(self, artist):
        tmp = {}
        if artist != "":
            print(artist.lower())
            for person in self.search:
                if re.search(artist.lower(), str(person)) != None:
                    print(self.search[person][0])
                    tmp[self.search[person][0]] = self.search[person][1]
            return tmp
        else:
            return tmp


    def add_song(self, artist, album, song, lyrics):
        print(artist)
        if artist not in self.artists:
            self.artists[artist] = {}
        if album not in self.artists[artist]:
            self.artists[artist][album] = {}
        if song not in self.artists[artist][album]:
            self.artists[artist][album][song] = {}
            for word in re.split('\n| ',lyrics):
                for char in self.notword:
                    word = word.replace(char,"")

                if word.lower() not in self.artists[artist][album][song]:
                    self.artists[artist][album][song][word.lower()] = 1
                else:
                    self.artists[artist][album][song][word.lower()] += 1

    def get_artists(self):
        tmp = []
        for artist in self.artists:
            tmp.append(artist)
        return tmp

    def remove_song(self, artist, album, song):
        if artist in self.artists:
            if album in self.artists[artist]:
                if song in self.artists[artist][album]:
                    del self.artists[artist][album][song]
                else:
                    raise ReferenceError('Song not found')
            else:
                raise ReferenceError('Album not found')
        else:
            raise ReferenceError('Artist not found')

    def remove_album(self, artist, album):
        if artist in self.artists:
            if album in self.artists[artist]:
                del self.artists[artist][album]
            else:
                raise ReferenceError('Album not found')
        else:
            raise ReferenceError('Artist not found')

    def remove_artist(self, artist):
        if artist in self.artists:
            del self.artists[artist]
        else:
            raise ReferenceError('Album not found')

    def empty(self):
        self.artists = {}

    def get_words_artist(self, artist):
        tmp = {}
        if artist in self.artists:
            for albums in self.artists[artist]:
                for songs in self.artists[artist][albums]:
                    for words in self.artists[artist][albums][songs]:
                        if words not in tmp:
                            tmp[words] = self.artists[artist][albums][songs][words]
                        else:
                            tmp[words] += self.artists[artist][albums][songs][words]
        else:
            raise ReferenceError('Artist not found')
        return tmp

    def get_words_album(self, artist, album):
        tmp = {}
        if artist in self.artists:
            if album in self.artists[artist]:
                for songs in self.artists[artist][album]:
                    for words in self.artists[artist][album][songs]:
                        if words not in tmp:
                            tmp[words] = self.artists[artist][album][songs][words]
                        else:
                            tmp[words] += self.artists[artist][album][songs][words]
            else:
                raise ReferenceError('Album not found')
        else:
            raise ReferenceError('Artist not found')
        return tmp

    def get_words_song(self, artist, album, song):
        tmp = {}
        if artist in self.artists:
            if album in self.artists[artist]:
                if song in self.artists[artist][album]:
                    for words in self.artists[artist][album][song]:
                        if words not in tmp:
                            tmp[words] = self.artists[artist][album][song][words]
                        else:
                            tmp[words] += self.artists[artist][album][song][words]
                else:
                    raise ReferenceError('Song not found')
            else:
                raise ReferenceError('Album not found')
        else:
            raise ReferenceError('Artist not found')
        return tmp

    def save(self, file):
        with open(file,'w') as f:
            json.dump(self.artists,f)

    def open(self, file):
        with open(file) as f:
            self.artists = json.load(f)

    def import_file(self,file):
        with open(file) as f:
            tmp = json.load(f)
            for artist in tmp:
                for album in tmp[artist]:
                    for song in tmp[artist][album]:
                        string = ""
                        for word in tmp[artist][album][song]:
                            print(word)
                            if artist not in self.artists:
                                self.artists[artist] = {}
                            if album not in self.artists[artist]:
                                self.artists[artist][album] = {}
                            if song not in self.artists[artist][album]:
                                self.artists[artist][album][song] = {}
                            if word.lower() not in self.artists[artist][album][song]:
                                self.artists[artist][album][song][word.lower()] = tmp[artist][album][song][word]



# add overloaded functions to get the unique word count total word counts and unique words
# maybe additionally overload a remove function
# maybe also a print function? although that seems less worth while

if __name__ == "__main__":
#    print('hello')
    test = lyrics()
    test.add_song("eh12ksdf", "asdf", "asdfsa", "alskfjd asdfa asfd asfd")
    test.save("testing1")
    test.empty()
    test.open("testing1")
    print(test.get_artists())
    print(test.artists)
    test.import_file("testing1")
    print(test.artists)
    print(test.get_artists())
    print("test")
    test.search_artist("zz")
    test.search_artist("a")
    test.search_artist("b")
    test.search_artist("a")
    print(test.search_artist(""))

#    print(test.artists)
#    print(test.get_words_artist("ehlaksdf"))
#    print(test.get_artists())
#    #test.remove_song("asdf", "asdfasfd", "asdfasdf")
