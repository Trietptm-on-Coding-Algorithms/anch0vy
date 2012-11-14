# -*- coding: cp949 -*-
import httplib
import urllib
import re


c_user = ''

def send_stop(site_cookie,session_id):
    global c_user
    host = 'www.facebook.com'
    n = 0
    if c_user == '':
        tmp = site_cookie.split('; ')
        for s in tmp:
            if s[0] == 'c':
                c_user = tmp[n]
            else:
                n = n + 1
        if c_user == '':
            print '잘못된 쿠키 파일'
            exit()
    c_user = '_' + c_user[1:]
    params = 'session_id='+str(session_id)+'&'+c_user+'&__a=1&fb_dtsg=AQD9ZuU8&phstamp=16581685790117855654'
    print params
    headers = {'Accept':'*/*','Content-Typ':'application/x-www-form-urlencoded','User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko)','Origin':'https://www.facebook.com','Accept-Encoding':'deflate','Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4','Accept-Charset':'windows-949,utf-8;q=0.7,*;q=0.3','Cookie':str(site_cookie),'Content-Length':str(len(params))}
    conn=httplib.HTTPSConnection(host)
    conn.request('POST','/ajax/settings/security/sessions/stop.php',params,headers)
    response = conn.getresponse()
    #print response.getheaders()
    print response.read()
    print response.status, response.reason
    conn.close()

f_cookie = raw_input('쿠키 파일: ')
f_cookie = open(f_cookie)
cookie = f_cookie.read()
f_cookie.close()

for n in range(0,10):
    send_stop(cookie,n+60)
    print n+60,'세션 종료'
