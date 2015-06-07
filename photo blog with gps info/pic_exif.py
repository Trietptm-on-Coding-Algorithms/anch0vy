import exifread,time
from StringIO import StringIO

def parse_gps(v,r):
	a=float(v[0].num)
	b=float(v[1].num)
	c=float(v[2].num)/v[2].den
	re=a+b/60+c/3600
	if r=='E' or r=='N':
		return re
	else:
		return -re

def get_pic_info(pic):
	if not hasattr(pic,'read'):
		pic=StringIO(pic)
	pic=exifread.process_file(pic)
	try:
		_long=pic['GPS GPSLongitude'].values
		_lat=pic['GPS GPSLatitude'].values
		_long_ref=pic['GPS GPSLongitudeRef'].values
		_lat_ref=pic['GPS GPSLatitudeRef'].values
		_long=parse_gps(_long,_long_ref)
		_lat=parse_gps(_lat,_lat_ref)
	except:
		_long,_lat=0,0#https://www.google.co.kr/maps/place/0%C2%B000%2700.0%22N+0%C2%B000%2700.0%22E/@4.6876379,11.4464934,3z/data=!4m2!3m1!1s0x0:0x0
	try:
		d=pic['EXIF DateTimeDigitized'].values
		d=time.strptime(d,'%Y:%m:%d %H:%M:%S')
		timestamp=int(time.mktime(d))
	except:
		timestamp=-1
	return _lat,_long,timestamp