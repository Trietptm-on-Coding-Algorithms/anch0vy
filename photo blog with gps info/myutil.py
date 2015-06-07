import time,datetime
from dbtool import dbtool
from pic_exif import get_pic_info
from image_process import image_write
from setting import ALLOWED_EXTENSIONS

def timestamp2str(date):
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(date))

def save_data(datas):
	db=dbtool()
	for subject,date,content,pics in datas:
		if not isinstance(subject,unicode):
			subject=unicode(subject,'utf-8')
		if not isinstance(content,unicode):
			content=unicode(content,'utf-8')
		_pic_num=[]
		for md5,pic in pics:
			image_write(md5,pic)
			_lat,_long,timestamp=get_pic_info(pic)
			db.insert_picture_info(timestamp,_long,_lat,md5+'.jpg')
			db.execute('SELECT pid FROM picture WHERE filename=?',(md5+'.jpg',))
			_pic_num.append(db.fetchone()[0])
		pic_num=map(str,_pic_num)
		db.insert_article_info(subject,content,','.join(pic_num),date)
	db.commit()
	db.close()
	return 'OK!'

def check_admin(session):
	if session.has_key('admin') and session['admin']:
		return True
	else:
		return False

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def str2datetime(_str):
	y=int(_str[:2])+2000
	m=int(_str[2:4])
	d=int(_str[4:])
	return datetime.date(y,m,d)