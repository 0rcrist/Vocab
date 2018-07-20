import json
class lyrics:

    def __init__(self):
        self.artists = {}

    def add_song(self, artist, album, song, lyrics):
        if artist not in self.artists:
            self.artists[artist] = {}
        if album not in self.artists[artist]:
            self.artists[artist][album] = {}
        if song not in self.artists[artist][album]:
            self.artists[artist][album][song] = {}
            for word in lyrics.split(" "):
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

    def save(self):
        with open('save','w') as f:
            json.dump(self.artists,f)

    def open(self):
        with open('save') as f:
            self.artists = json.load(f)

# add overloaded functions to get the unique word count total word counts and unique words
# maybe additionally overload a remove function
# maybe also a print function? although that seems less worth while

if __name__ == "__main__":
#    print('hello')
    test = lyrics()
    test.add_song("ehlaksdf", "asdf", "asdfsa", "alskfjd asdfa asfd asfd")
    test.save()
    test.empty()
    test.open()
    print(test.get_artists())
#    print(test.artists)
#    print(test.get_words_artist("ehlaksdf"))
#    print(test.get_artists())
#    #test.remove_song("asdf", "asdfasfd", "asdfasdf")
