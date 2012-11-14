# -*- coding: cp949 -*-
import httplib
import urllib
import re


c_user = ''

def send_stop(site_cookie,session_id,c_user):
    __user = '_' + c_user[1:]
    params = 'session_id='+str(session_id)+'&'+c_user+'&__a=1&fb_dtsg=AQD9ZuU8'
    print params
    headers ={}
    headers['Connection']='keep-alive'
    headers['Content-Length']=str(len(params))
    headers['User-Agent']='NONE'
    headers['Content-Type']='application/x-www-form-urlencoded'
    headers['Accept']='*/*'
    headers['Referer']='https://www.facebook.com/settings?tab=security&section=sessions&view'
    headers['Accept-Encoding']='deflate'
    headers['Accept-Language']='ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4'
    headers['Accept-Charset']='windows-949,utf-8;q=0.7,*;q=0.3'
    headers['Cookie']=site_cookie
    headers['Host']='www.facebook.com'
    conn=httplib.HTTPSConnection(host)
    conn.request('POST','/ajax/settings/security/sessions/stop.php',params,headers)
    response = conn.getresponse()
    #print response.getheaders()
    print response.read()
    print response.status, response.reason
    conn.close()
    raw_input('step')#debug

def get_info(site_cookie):
    tmp = site_cookie.split('; ')
    n = 0
    for s in tmp:
        if s[0] == 'c':
            c_user = tmp[n]
        else:
            n = n + 1
    if c_user == '':
        print '잘못된 쿠키 파일'
        exit()
    host = 'm.facebook.com'
    headers ={}
    headers['Connection']='keep-alive'
    headers['User-Agent']='NONE'
    headers['Content-Type']='application/x-www-form-urlencoded'
    headers['Accept']='*/*'
    headers['Referer']='https://www.facebook.com/settings?tab=security&section=sessions&view'
    headers['Accept-Encoding']='deflate'
    headers['Accept-Language']='ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4'
    headers['Accept-Charset']='windows-949,utf-8;q=0.7,*;q=0.3'
    headers['Cookie']=site_cookie
    headers['Host']='m.facebook.com'
    conn=httplib.HTTPSConnection(host)
    conn.request('GET','/ajax/dtsg.php','',headers)
    response = conn.getresponse()
    print response.getheaders()
    raw_input('step')#debug
    print response.read()
    raw_input('step')#debug
    print response.status, response.reason
    raw_input('step')#debug
    conn.close()

    

f_cookie = raw_input('쿠키 파일: ') 
f_cookie = open(f_cookie)
cookie = f_cookie.read()
f_cookie.close()
print cookie#debug
get_info(cookie)
raw_input('step')#debug

for n in range(0,10):
    send_stop(cookie,n+60)
    print n+60,'세션 종료'
