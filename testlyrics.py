import unittest
from lyrics import lyrics

class Testlyrics(unittest.TestCase):
    def test_add(self):
        tmp = lyrics()
        tmp.add_song("Toto", "Toto IV", "africa", "I hear the drums echoing tonight \
But she hears only whispers of some quiet conversation \
Shes coming in 12:30 flight ")
        self.assertEqual(tmp.get_words_artist("Toto"), {'i': 1, 'hear': 1, 'the': 1, 'drums': 1, 'echoing': 1, 'tonight': 1, 'but': 1, 'she': 1, 'hears': 1, 'only': 1, 'whispers': 1, 'of': 1, 'some': 1, 'quiet': 1, 'conversation': 1, 'shes': 1, 'coming': 1, 'in': 1, '12:30': 1, 'flight': 1, '': 1} )

    def test_get_artists(self):
        tmp = lyrics()
        tmp.add_song("Toto", "Toto IV", "africa", "I hear the drums")
        tmp.add_song("Disturbed", "immortalized", "The Sound of Silence", "Hello darkness my old friend")
        tmp.add_song("Eminem", "The Marshall Mathers LP 2", "Rap God", "Look I was gonna go easy on you and not to hurt your feelings")
        self.assertEqual(tmp.get_artists(), ['Toto', 'Disturbed', 'Eminem'])



    def test_exceptions(self):
        tmp = lyrics()
        tmp.add_song("Toto", "Toto IV", "africa", "I hear the drums")
        tmp.add_song("Disturbed", "immortalized", "The Sound of Silence", "Hello darkness my old friend")
        tmp.add_song("Eminem", "The Marshall Mathers LP 2", "Rap God", "Look I was gonna go easy on you and not to hurt your feelings")
        with self.assertRaises(ReferenceError):
            tmp.get_words_artist("Billy")
        with self.assertRaises(ReferenceError):
            tmp.get_words_album("Toto", "not real")
        with self.assertRaises(ReferenceError):
            tmp.get_words_song("Toto", "not real", "africa")
        with self.assertRaises(ReferenceError):
            tmp.get_words_song("Toto", "Toto IV", "not real")
        with self.assertRaises(ReferenceError):
            tmp.remove_artist("jimmy")
        with self.assertRaises(ReferenceError):
            tmp.remove_album("Toto", "Toto I")
        with self.assertRaises(ReferenceError):
            tmp.remove_song("Toto", "Toto IV", "nevada")

    def test_removing(self):
        tmp = lyrics()
        tmp.add_song("Toto", "Toto IV", "africa", "I hear the drums")
        tmp.add_song("Toto", "Toto IV", "nevada", "I hear the drums")
        tmp.add_song("Disturbed", "immortalized", "The Sound of Silence", "Hello darkness my old friend")
        tmp.add_song("Disturbed", "immortalized", "The Sound", "old friend")
        tmp.add_song("Eminem", "The Marshall Mathers LP 2", "Rap God", "Look I was gonna go easy on you and not to hurt your feelings")
        tmp.remove_song("Toto", "Toto IV", "africa")
        self.assertEqual(tmp.artists,{'Toto': {'Toto IV': {'nevada': {'i': 1, 'hear': 1, 'the': 1, 'drums': 1}}}, 'Disturbed': {'immortalized': {'The Sound of Silence': {'hello': 1, 'darkness': 1, 'my': 1, 'old': 1, 'friend': 1}, 'The Sound': {'old': 1, 'friend': 1}}}, 'Eminem': {'The Marshall Mathers LP 2': {'Rap God': {'look': 1, 'i': 1, 'was': 1, 'gonna': 1, 'go': 1, 'easy': 1, 'on': 1, 'you': 1, 'and': 1, 'not': 1, 'to': 1, 'hurt': 1, 'your': 1, 'feelings': 1}}}})
        tmp.remove_album("Disturbed", "immortalized")
        self.assertEqual(tmp.artists,{'Toto': {'Toto IV': {'nevada': {'i': 1, 'hear': 1, 'the': 1, 'drums': 1}}}, 'Disturbed': {}, 'Eminem': {'The Marshall Mathers LP 2': {'Rap God': {'look': 1, 'i': 1, 'was': 1, 'gonna': 1, 'go': 1, 'easy': 1, 'on': 1, 'you': 1, 'and': 1, 'not': 1, 'to': 1, 'hurt': 1, 'your': 1, 'feelings': 1}}}})
        tmp.remove_artist("Toto")
        tmp.save()
        self.assertEqual(tmp.artists,{'Disturbed': {}, 'Eminem': {'The Marshall Mathers LP 2': {'Rap God': {'look': 1, 'i': 1, 'was': 1, 'gonna': 1, 'go': 1, 'easy': 1, 'on': 1, 'you': 1, 'and': 1, 'not': 1, 'to': 1, 'hurt': 1, 'your': 1, 'feelings': 1}}}} )
        tmp.empty()
        self.assertEqual(tmp.artists, {})


