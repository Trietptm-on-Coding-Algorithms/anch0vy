# -*- coding: cp949 -*-

#쿠키값은 모조리 사용자가 집어넣는걸로 함
#TODO: 쿠키값 자동으로 얻어오기

import httplib
import urllib
import re
import sys


headers ={}
headers['Connection']='keep-alive'
headers['User-Agent']='NONE'
headers['Content-Type']='application/x-www-form-urlencoded'
headers['Accept']='*/*'
headers['Referer']='https://www.facebook.com/settings?tab=security&section=sessions&view'
headers['Accept-Encoding']='deflate'
headers['Accept-Language']='ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4'
headers['Accept-Charset']='windows-949,utf-8;q=0.7,*;q=0.3'
headers['Host']='www.facebook.com'


def send_stop(headers,session_id,c_user,xs,fb_dtsg):
    __user = '_' + c_user[1:]
    params = 'session_id='+str(session_id)+'&'+__user + '&' + 'fb_dtsg=' + fb_dtsg
    headers['Content-Length']=str(len(params))
    headers['Cookie']= 'c_user=' + c_user + '; '+ 'xs=' + xs + ';'
    print headers['Cookie']#debug
    conn=httplib.HTTPSConnection('www.facebook.com')
    conn.request('POST','/ajax/settings/security/sessions/stop.php',params,headers)
    print params#debug
    response = conn.getresponse()
    print response.read()#debug
    print response.status, response.reason
    conn.close()

def get_fb_dtsg(headers,c_user,xs):
    headers['Cookie']= 'c_user=' + c_user + '; '+ 'xs=' + xs + ';'
    conn=httplib.HTTPSConnection('www.facebook.com')
    conn.request('GET','/asdf','',headers)
    response = conn.getresponse()
    page = response.read()
    print response.status, response.reason
    conn.close()
    fb_dtsg = re.findall('''"hidden" name="fb_dtsg" value="(.*?)"''',page,re.DOTALL)
    print 'fb_dtsg :',fb_dtsg[0]
    return fb_dtsg[0]

if len(sys.argv) != 3:
    print '사용법: 프로그램명 xs c_user'
    print '사용법 예: facebook.py 1%3ATlTDZM...중략...A1352804488 10...중략....9'
    exit()
    
xs = str(sys.argv[1])
c_user = str(sys.argv[2])

fb_dtsg = get_fb_dtsg(headers,c_user,xs)

for n in range(60,70):
    send_stop(headers,n,c_user,xs,fb_dtsg)
    print n,'번 세션 종료'
raw_input('end')
    
