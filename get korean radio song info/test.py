import urllib
from bs4 import BeautifulSoup
_url='http://radio.sbs.co.kr/music/wizard_broadcast_new.jsp?position_code=%s&year=%d&month=%d&day=%d'
bs=BeautifulSoup((urllib.urlopen(_url%('night_yewon',2014,11,30))))
bs=bs.tbody
for x in bs.find_all('span'):
        x.extract()
for x in bs.find_all('td',class_='account'):
        x.extract()
for x in bs.find_all('th'):
        x.extract()
bs=bs.find_all('tr')
for song in bs:
    song=song.find_all('td')
    if len(song)>1:
        print song[1].text,song[0].text
