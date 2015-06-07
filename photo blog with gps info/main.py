# -*- coding: utf-8 -*-
import os,time,json,hashlib,datetime

from flask import Flask,request,send_file,_app_ctx_stack,render_template,session,redirect,url_for
from werkzeug import secure_filename

from setting import USER,PASSWD,SHOW_ARTICLE_NUM_AT_ONE_PAGE,ADMIN_PASSWORD,UPLOAD_FOLDER
from dbtool import userdb_init,dbopen,dbtool
from StringIO import StringIO
from mail import get_from_mails
from myutil import timestamp2str,save_data,check_admin,allowed_file,str2datetime
SANAOP=SHOW_ARTICLE_NUM_AT_ONE_PAGE

if not os.path.isfile('user.db'):
	userdb_init()

if not os.path.isfile('radio.db'):
	radiodb_init()

db_stack=[]
app = Flask(__name__)
app.secret_key='\xab\xcc\xde\x43\x66\xbai_love_python'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(403)
@app.errorhandler(410)
@app.errorhandler(500)
def ggil_ggil(e):
	ret=[]
	ret.append('<b>Page Not Found</b><br>')
	ret.append('........')
	ret.append('<br><br><br><br><br>')
	return '\n'.join(ret)

@app.teardown_appcontext
def close_connection(exception):
	try:
		db=db_stack.pop()
		db.close()
	except:
		pass

@app.route('/favicon.ico')
def favicon():
	return send_file('favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/')
@app.route('/<int:article_num>')
def home(article_num=-1):
	SANAOP=SHOW_ARTICLE_NUM_AT_ONE_PAGE
	ret=[]
	dc=0
	db=dbtool()
	db_stack.append(db)
	page={}
	db.execute('SELECT count(*) from board')
	article_all_num=db.fetchone()[0]
	page_num=request.args.get('page')
	if page_num==None:
		page['now']=1
	else:
		page['now']=int(page_num)
	if page['now']-5 < 1:
		n=1
	else:
		n=page['now']-5
	page['all']=range(n,article_all_num/SANAOP+1+bool(article_all_num%SANAOP))[:11]
	if article_num==-1:
		article_list=db.read_article_with_limit(page['now'],SHOW_ARTICLE_NUM_AT_ONE_PAGE)
	else:
		article_list=db.read_article_with_article_number(article_num)
	for aid,title,content,pic_num,article_date in article_list:
		article_date=timestamp2str(article_date)
		__pics=pic_num.split(',')
		pics=[]
		if len(__pics)==1 and __pics[0]==u'':
			pass
		else:
			_pics=map(int,__pics)
			for pid in _pics:
				pic_date,longitude,latitude,filename,deleted=db.read_picture_with_pid(pid)
				if deleted==0:
					pic_date=timestamp2str(pic_date)
					pics.append({'pid':pid,'pic_date':pic_date,'longitude':longitude,'latitude':latitude,'filename':filename})
		ret.append({'aid':aid,'title':title,'content':content,'article_date':article_date,'pics':pics})
	_info=db.get_blog_info()
	info={'intro':_info[0],'nickname':_info[1]}
	if request.args.get('new'):
		return render_template('./index.html',ret=ret,page=page,session=session,info=info)
	return render_template('./new.html',ret=ret,page=page,session=session,info=info)


@app.route('/radio/<date>')
@app.route('/radio')
def radio(date='now'):
	oneday=datetime.timedelta(days=1)
	if date=='now':
		yesterday=datetime.date.today()-oneday
		_next=datetime.date.today().strftime('%y%m%d')
		_pre=datetime.date.today()-oneday-oneday
		_pre=_pre.strftime('%y%m%d')
		date=yesterday.strftime('%y%m%d')
		print date
		_date=yesterday.strftime('%y.%m.%d')
	else:
		_date='%s.%s.%s'%(date[:2],date[2:4],date[4:])
		date=str2datetime(date)
		_next=date+oneday
		_next=_next.strftime('%y%m%d')
		_pre=date-oneday
		_pre=_pre.strftime('%y%m%d')
		date=date.strftime('%y%m%d')
	ret=[]
	db=dbtool('radio.db')
	_programs={}
	for programMasterName,channelName,programId,broadcastTime in db.get_recent_program(date):
		d={}
		d['programMasterName']=programMasterName
		d['programId']=programId
		d['broadcastTime']=broadcastTime[:2]+':'+broadcastTime[2:]
		if _programs.has_key(channelName):
			_programs[channelName].append(d)
		else:
			_programs[channelName]=[]
			_programs[channelName].append(d)
	programs=_programs.items()
	programs.sort()
	if request.args:
		where=request.args.to_dict()
		where['date']='20'+date
	#channelId,channelName,programId,programMasterName,title,artistName,broadcastTime,youtube
		for song in db.read_song(where):
			d={}
			d['date']=song[0]
			d['channelId']=song[1]
			d['channelName']=song[2]
			d['programId']=song[3]
			d['programMasterName']=song[4]
			d['title']=song[5]
			d['artistName']=song[6]
			d['broadcastTime']=song[7]
			d['youtube']=song[8]
			ret.append(d)
	return render_template('./radio.html',ret=ret,programs=programs,date=_date,next=_next,pre=_pre,session=session)

@app.route('/all')
def all():
	ret=[]
	db=dbopen()
	db_stack.append(db)
	cur=db.cursor()
	cur.execute('SELECT date,longitude,latitude,filename from picture')
	for date,longitude,latitude,filename in cur.fetchall():
		ret.append({'date':date,'longitude':longitude,'latitude':latitude,'filename':filename})
	return render_template('./map.html',ret=ret)


@app.route('/mailcheck')
def mailcheck():
	dc=0
	db=dbtool()
	db_stack.append(db)
	#ret -> (subject,date(unix_time_stamp),content,pics)
	mails=get_from_mails()
	return save_data(mails)

@app.route('/write',methods=['POST'])
def write():
	if check_admin(session) and request.method=='POST':
		ret=[]
		pics=[]
		print repr(request.form)
		subject=request.form['title']
		content=request.form['content']
		uploaded_files = request.files.getlist("file")
		for file in uploaded_files:
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				pic=file.read()
				_md5=hashlib.md5(pic).hexdigest()
				pics.append([_md5,pic])
		ret.append([subject,int(time.time()),content,pics])
		return save_data(ret)
	else:
		return redirect('admin')


@app.route('/edit',methods=['POST'])
def edit():
	if check_admin(session):
		request.files.getlist("file[]")
	else:
		return redirect(url_for('admin'))


@app.route('/admin',methods=['GET','POST'])
def admin():
	if check_admin(session):
		return redirect(url_for('home'))
	else:
		if request.method == 'POST':
			print '[!]form:',request.form['my_name']
			if request.form['my_name'] == ADMIN_PASSWORD:
				session['admin']=True
				return redirect(url_for('home'))
			else:
				return render_template('./admin.html')
		else:
			return render_template('./admin.html')


@app.route('/delete/article/<int:article_num>')
def delete_article(article_num):
	if check_admin(session):
		db=dbtool()
		db.delete_article(article_num)
		return '<script>history.back()</script>'
	else:
		return redirect(url_for('admin'))

@app.route('/delete/picture/<int:picture_num>')
def delete_picture(picture_num):
	if check_admin(session):
		db=dbtool()
		db.delete_picture(picture_num)
		return '<script>history.back()</script>'
	else:
		return redirect(url_for('admin'))



@app.route('/logout')
def logout():
	session['admin']=False
	del(session['admin'])
	return redirect(url_for('home'))


@app.route('/pic/<filename>')
def send_image(filename):
	return send_file('pic/'+filename, mimetype='image/jpeg')

@app.route('/static/<filename>')
def send_static(filename):
	return send_file('static/'+filename)

@app.route('/<path:filename>')
def root(filename):
	#return filename
	return send_file(filename)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)