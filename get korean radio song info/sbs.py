from bs4 import BeautifulSoup
import urllib
bs=BeautifulSoup((urllib.urlopen('http://w3.sbs.co.kr/schedule/scheduleSub.do?depth02=d2_3&depth03=love&channel=Love')))
bs=bs.tbody
for x in bs.find_all('a'):
    print '["sbs_power_fm",u"%s","","%s","","",""]'%(x.get_text().replace('\n','').replace('\t','').replace('\x0d',''),x.get('href'))
