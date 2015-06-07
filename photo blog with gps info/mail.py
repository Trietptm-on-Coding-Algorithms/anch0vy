import poplib,email,hashlib,time
from email.header import decode_header
from email.utils import parsedate,parsedate_tz
from setting import MAIL_SENDER,MAIL_SERVER_ID,MAIL_SERVER_PASSWD
import pic_exif

def connect_mail_server():
	mail_con = poplib.POP3_SSL('localhost')
	mail_con.user(MAIL_SERVER_ID)
	mail_con.pass_(MAIL_SERVER_PASSWD)
	return mail_con

def get_mails():
	mail_con=connect_mail_server()
	num = mail_con.stat()[0]
	ret=[]
	for i in range(1,1+num):
		msg=mail_con.retr(i)[1]
		msg_parsed=email.message_from_string('\n'.join(msg))
		if MAIL_SENDER in msg_parsed['From']:
			mail_con.dele(i)
			ret.append((i,msg_parsed))
	mail_con.quit()
	return ret

def all_decode_header(s):
	ret=[]
	for _str,encode in decode_header(s):
		if encode==None:
			ret.append(unicode(_str).encode('utf-8'))
		else:
			ret.append(unicode(_str,encode).encode('utf-8'))
	return ''.join(ret)

def change_date_format(s):
	d=parsedate(s)
	r=time.mktime(d)
	return int(r)

def _get_from_mails(mails):
	#ret -> (subject,date(unix_time_stamp),content,pics)
	ret=[]
	for i,msg in mails:
		content=[]
		pics=[]
		subject=all_decode_header(msg['Subject'])
		date=change_date_format(msg['date'])
		for msg_part in msg.walk():
			_type=msg_part.get_content_type()
			if _type=='image/jpeg': #image
				pic=msg_part.get_payload(decode=True)
				md5=hashlib.md5(pic).hexdigest()
				pics.append((md5,pic))
			elif _type=='text/plain' and not msg_part.has_key('Content-Disposition'): #content
				tmp=msg_part.get_payload(decode=True)
				if 'euc-kr' in msg_part['Content-Type']:
					_content=unicode(tmp,'euc-kr')
				elif 'utf-8' in msg_part['Content-Type'] or 'UTF-8' in msg_part['Content-Type']:
					_content=unicode(tmp,'utf-8')
				else:
					_content=unicode(tmp)
				content.append(_content.encode('utf-8'))
			else:
				continue
		full_content=''.join(content)
		full_content=full_content.replace('\r','')
		while '\n\n' in full_content:
			full_content=full_content.replace('\n\n','\n')
		ret.append((subject,date,full_content,pics))
	return ret

def get_from_mails():
	mails = get_mails()
	return _get_from_mails(mails)
