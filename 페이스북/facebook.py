# -*- coding: cp949 -*-

#일단 크롬만 지원을 목표

import httplib
import urllib
import re


c_user = ''

def send_stop(site_cookie,session_id,c_user,xs,fb_dtsg):
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
    conn=httplib.HTTPSConnection('www.facebook.com')
    conn.request('POST','/ajax/settings/security/sessions/stop.php',params,headers)
    response = conn.getresponse()
    #print response.getheaders()
    print response.read()
    print response.status, response.reason
    conn.close()
    raw_input('step')#debug

def get_fb_dtsg(site_cookie):
    site_cookie = site_cookie + ' xs=1%3AWaMJ6hll-ZbjeQ%3A2%3A1352879656;'
    print site_cookie
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
    headers['Host']='www.facebook.com'
    conn=httplib.HTTPSConnection('m.facebook.com')
    conn.request('GET','/ajax/dtsg.php','',headers)
    response = conn.getresponse()
    t = response.read()
    print t
    regex = re.compile('''type=\"hidden\" name=\"fb_dtsg\" value=\"(.*?)\"''')
    fb_dtsg = regex.findall(t)
    #fb_dtsg = fb_dtsg[0]
    print fb_dtsg #debug

f_cookie = raw_input('쿠키 파일: ') 
f_cookie = open(f_cookie)
cookie = f_cookie.read()
f_cookie.close()
#print cookie#debug
get_fb_dtsg(cookie)
raw_input('step')#debug

for n in range(0,10):
    send_stop(cookie,n+60)
    print n+60,'세션 종료'
