from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

r = urlopen('https://www.azlyrics.com/e/eminem.html')
soup = bs(r)

print(soup)