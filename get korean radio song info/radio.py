# -*- coding: utf-8 -*-
from flask import Flask,request,send_file,_app_ctx_stack
from bs4 import BeautifulSoup
import urllib,feedparser,re,datetime,json
import youtube
from radio_list import rlist
from dbtool import dbopen,dbclose,create_program_table,insert_song2db
app = Flask(__name__)
dbstack=[]
@app.teardown_appcontext
def close_connection(exception):
	if dbstack==[]:
		pass
	else:
		db=dbstack.pop()
		db.close()

@app.route('/')
def home():
	db=dbopen()
	dbstack.append(db)
	ret=[]
	for broad,title,broad_time,option1,option2,option3,option4 in rlist:
		print broad,title,
		create_program_table(db,broad,title)
		if broad.startswith('kbs'):
			songlist=kbs_getsonglist(option1,option2)
		elif broad.startswith('mbc'):
			songlist=mbc_getsonglist(option1,option2)
		elif broad.startswith('sbs'):
			songlist=sbs_getsonglist(option1)

		else:
			continue

		for songs,date in songlist:
			print date
			ret.append(date)
			for artist,song_title in songs:
				insert_song2db(db,title,date,artist,song_title)
	return '\n'.join(ret)

def sbs_getsonglist(broad_code):
	ret=[]
	now=datetime.datetime.now()
	oneday=datetime.timedelta(days=1)
	for d in range(3):
		songs=[]
		now=now-oneday
		date='%d-%d-%d'%(now.year,now.month,now.day)
		_url='http://radio.sbs.co.kr/music/wizard_broadcast_new.jsp?position_code=%s&year=%d&month=%d&day=%d'
		bs=BeautifulSoup((urllib.urlopen(_url%(broad_code,now.year,now.month,now.day))))
		bs=bs.tbody
		for x in bs.find_all('span'):
			x.extract()
		for x in bs.find_all('td',class_='account'):
			x.extract()
		for x in bs.find_all('th'):
			x.extract()
		bs=bs.find_all('tr')
		for x in bs:
			song=x.find_all('td')
			if len(song)>1:
				#print song[1].text,song[0].text
				songs.append([song[1].text,song[0].text])
		ret.append([songs,date])
	return ret
def mbc_getsonglist(gid,bid):
	ret=[]
	_url='http://miniunit.imbc.com/list/musicitemlist?rtype=jsonp&bid=%s&gid=%s&bdate=%s'
	now=datetime.datetime.now()
	oneday=datetime.timedelta(days=1)
	for x in range(3):
		songs=[]
		now=now-oneday
		bdate='%d-%d-%d'%(now.year,now.month,now.day)
		url=_url%(bid,gid,bdate)
		try:
			js=json.load(urllib.urlopen(url))
		except:
			js=-1
		if js != [] and js != -1:
			for j in js:
				songs.append([j['ArtistName'],j['TrackTitle']])
		ret.append([songs,bdate])
	return ret

def kbs_getsonglist(channelId,programId):
	ret=[]
	_url='http://music.daum.net/onair/programScheduleSongList.json?searchDate=%s&channelId=%s&mediaType=4&programId=%s'
	now=datetime.datetime.now()
	oneday=datetime.timedelta(days=1)
	for x in range(3):
		songs=[]
		now=now-oneday
		date='%d-%d-%d'%(now.year,now.month,now.day)
		_date='%d%d%d'%(now.year,now.month,now.day)
		url=_url%(_date,channelId,programId)
		try:
			js=json.load(urllib.urlopen(url))
		except:
			js=-1
		if js != [] and js != -1:
			for j in js['songList']:
				songs.append([j['artistName'],j['title']])
		ret.append([songs,date])
	return ret

def old_kbs_getsonglist(_feed,_filter="\.(.*?)\n",must_have_word='',block_word=''):
	if block_word=='':
		block_word='navdaksjvjsdvafjvbnakjsghakjsfdh'
	block_word=re.compile(block_word)
	feed = feedparser.parse(_feed)
	ret=[]
	for n in range(3):
		entry=feed.entries[n]
		soup = BeautifulSoup(entry.description)
		soup=soup.get_text("\n",strip=True)
		soup=soup.split('\n')
		rr=[]
		for x in soup:
			if bool(block_word.search(x))==False and check_str_must_have_words(x,must_have_word) and len(x) > 3:
				rr.append(x)
		ret.append([rr,entry['published']])
	return ret


def check_str_must_have_words(_str,must_have_word):
	if type(must_have_word)==type([]):
		for word in must_have_word:
			if not bool(word in _str):
				return False
	else:
		return bool(must_have_word in _str)
	return True


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)