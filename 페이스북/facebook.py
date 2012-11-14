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
    h = httplib.HTTP(host)
    h.putrequest('POST','/ajax/settings/security/sessions/stop.php',params)
    h.putheader('Host', host)
    h.putheader('User-Agent', '''Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.152 Safari/535.19 CoolNovo/2.0.3.55''')
    #크롬 헤더임
    h.putheader('Accept','text/html')
    h.putheader('Referer','https://www.facebook.com/settings?tab=security&section=sessions&view')
    h.putheader('Cookie',site_cookie)
    h.endheaders()
    errorCode, errorMessage, headers = h.getreply()
    a = h.getfile()
    text_tmp = a.read()
    h.close()

f_cookie = raw_input('쿠키 파일: ')
cookie = f_cookie.read()
f_cookie.close()

for n in range(0,10):
    send_stop(cookie,n+60)
    print n+60,'세션 종료'
