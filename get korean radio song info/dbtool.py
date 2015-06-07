import MySQLdb
#import sqlite3
import json	
import youtube
def dbopen():
	db=MySQLdb.connect('localhost','root','erased','radio',charset='utf8', use_unicode=True)
	cur=db.cursor()
	cur.execute("set names utf8")
	return db

def dbclose(db):
	db.close()

def create_program_table(db,broad,_title,time=''):
	c=0
	cur=db.cursor()
	title=_title.replace(' ','_').replace(',','_')
	q='CREATE TABLE %s (no int NOT NULL AUTO_INCREMENT PRIMARY KEY, date_ TEXT, youtube_url TEXT, youtube_title TEXT, artist TEXT, song_title TEXT);'%(title.replace(' ','_'))
	try:
		cur.execute(q)
	except:
		pass
	try:
		q="SELECT pid FROM programs WHERE db_title='%s';"%(title)
		cur.execute(q)
		if cur.fetchone():
			pass
		else:
			q="INSERT INTO programs (broad,db_title,real_title) VALUES('%s', '%s','%s');"%(broad,title,_title)
			cur.execute(q)
	except:
		print '[!]error 1at',q

def insert_song2db(db,_title,date_,artist,song_title):
	artist=get_safe_string(artist)
	song_title=get_safe_string(song_title)
	title=_title.replace(' ','_').replace(',','_')
	song=artist+' '+song_title
	if check_song(db,title,date_,song_title):
		youtube_title,youtube_url=youtube.youtube_search(unicode(song))
	else:
		return -1
	if youtube_title==-1:
		return -1

	youtube_title=get_safe_string(youtube_title)
	cur=db.cursor()
	q="INSERT INTO %s (date_,youtube_url,youtube_title,artist,song_title) VALUES('%s', '%s' , '%s','%s','%s');" %(title,date_,youtube_url,youtube_title,artist,song_title)
	try:
		cur.execute(q)
	except:
		print '[!]error at',q

def check_song(db,title,date_,song_title):
	cur=db.cursor()
	q="SELECT * FROM %s WHERE date_='%s' and song_title='%s';"%(title,date_,song_title)
	try:
		cur.execute(q)
		if cur.fetchone():
			print '!!',
			return False
		else:
			return True
	except:
		print '[!]error at',q
		return False

def get_safe_string(s):
	return s.replace("'","''")
