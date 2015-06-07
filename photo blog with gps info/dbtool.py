import sqlite3,time,datetime
from flask import abort

DEBUG=0
def dbopen(dbname):
	db=sqlite3.connect(dbname)
	return db


def userdb_init():
	db=dbopen('user.db')
	cur=db.cursor()
	cur.execute('''CREATE TABLE picture (
			pid INTEGER PRIMARY KEY, 
			date NUMERIC NOT NULL, 
			longitude NUMERIC NOT NULL, 
			latitude NUMERIC NOT NULL, 
			filename TEXT NOT NULL,
			deleted NUMERIC NULL
			);''')
	cur.execute('''CREATE TABLE board (
			aid INTEGER PRIMARY KEY, 
			title TEXT NOT NULL, 
			content TEXT NULL, 
			comment_num TEXT NULL, 
			pic_num TEXT NULL,
			article_date NUMERIC NOT NULL,
			deleted NUMERIC NULL
			);''')
	cur.execute('''CREATE TABLE comment (
			cid INTEGER PRIMARY KEY, 
			ip TEXT NOT NULL, 
			name TEXT NOT NULL, 
			cpasswd TEXT NOT NULL, 
			ccontent TEXT NOT NULL, 
			deleted NUMERIC NOT NULL
			);''')
	cur.execute('''CREATE TABLE blog_info (
			introduction TEXT,
			nickname NUMERIC
			);''')
	db.commit()
	db.close()

def radiodb_init():
	db=dbopen('radio.db')
	cur=db.cursor()
	cur.execute('''CREATE TABLE songlist (
			date TEXT,
			channelId TEXT,
			programId TEXT,
			programMasterName TEXT, 
			channelName TEXT,
			title TEXT,
			artistName TEXT,
			broadcastTime TEXT,
			youtube TEXT)
			;''')
	db.commit()
	db.close()

class dbtool():
	def __init__(self,dbname='user.db'):
		self.db=dbopen(dbname)
		self.cur=self.db.cursor()
		self.commit=self.db.commit
		self.close=self.db.close
		self.fetchall=self.cur.fetchall
		self.ex_query=''
		self.ex_arg=()

	def execute(self,q,arg=()):
		t=time.time()
		self.ex_query=q
		self.ex_arg=arg
		try:
			self.cur.execute(q,arg)
		except:
			print '[x]Query error:%s'%q
			print '[x]arg:',repr(arg)
			abort(500)
		if DEBUG:
			print '[!]Query: %s'%q
			print '[!]arg:',repr(arg)
			print '[!]time:',time.time()-t

	def fetchone(self):
		r=self.cur.fetchone()
		if len(r)==0:
			print '[x]error at fetchone'
			print '[x]query:',self.ex_query
			print '[x]arg:',repr(self.ex_arg)
		return r

	def __del__(self):
		self.close()

#blog
	def read_article_with_limit(self,now_page,SHOW_ARTICLE_NUM_AT_ONE_PAGE):
		now_page-=1
		q='SELECT aid,title,content,pic_num,article_date FROM board where deleted=0 order by article_date desc limit ?,?'
		self.execute(q,(now_page*SHOW_ARTICLE_NUM_AT_ONE_PAGE,now_page*SHOW_ARTICLE_NUM_AT_ONE_PAGE+SHOW_ARTICLE_NUM_AT_ONE_PAGE))
		return self.fetchall()

	def read_article_with_article_number(self,article_number):
		q='SELECT aid,title,content,pic_num,article_date FROM board where aid=?'
		self.execute(q,(article_number,))
		return self.fetchall()

	def read_picture_with_pid(self,picture_number):
		q='SELECT date,longitude,latitude,filename,deleted from picture where pid=?'
		self.execute(q,(picture_number,))
		return self.fetchone()

	def insert_picture_info(self,timestamp,_long,_lat,filename):
		q='INSERT INTO picture (date,longitude,latitude,filename,deleted) VALUES(?,?,?,?,0)'
		self.execute(q,(timestamp,_long,_lat,filename))

	def insert_article_info(self,subject,content,pic_nums,date):
		q='INSERT INTO board (title,content,pic_num,article_date,deleted) VALUES(?,?,?,?,0)'
		self.execute(q,(subject,content,pic_nums,date,))

	def delete_article(self,article_number):
		q='UPDATE board SET deleted=1 WHERE aid=?'
		self.execute(q,(article_number,))
		self.commit()

	def delete_picture(self,picture_number):
		q='UPDATE picture SET deleted=1 WHERE pid=?'
		self.execute(q,(picture_number,))
		self.commit()

	def get_blog_info(self):
		q='SELECT introduction,nickname FROM blog_info;'
		self.execute(q)
		return self.fetchone()

#radio
	def insert_song(self,song_dict):
		q='INSERT INTO songlist (date,channelId,programId,programMasterName,channelName,title,artistName,broadcastTime,youtube) VALUES(:date,:channelId,:programId,:programMasterName,:channelName,:title,:artistName,:broadcastTime,:youtube)'
		self.execute(q,song_dict)
		self.commit()

	def read_song(self,where_dict):
		q='SELECT date,channelId,channelName,programId,programMasterName,title,artistName,broadcastTime,youtube FROM songlist WHERE '
		l=where_dict.items()
		tmp=[]
		qq=[]
		for x in l:
			tmp.append('%s=?'%x[0])
			qq.append(x[1])
		q=q+' and '.join(tmp)
		print q
		self.execute(q,tuple(qq))
		return self.fetchall()

	def get_recent_program(self,date):
		q='SELECT distinct programMasterName,channelName,programId,broadcastTime from songlist where date = ? order by broadcastTime;'
		#yesterday=datetime.date.today()-(datetime.timedelta(days=1)*7)
		#date='%d%d%d'%(yesterday.year,yesterday.month,yesterday.day)
		self.execute(q,('20'+date,))
		return self.fetchall()