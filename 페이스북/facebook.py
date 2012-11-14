# -*- coding: cp949 -*-
import httplib
import urllib
import re
host = 'www.facebook.com'
h = httplib.HTTP(host)
h.putrequest('GET','/?PAGEKEY='+next_page)
h.putheader('Host', host)
h.putheader('User-Agent', '''Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.152 Safari/535.19 CoolNovo/2.0.3.55
''')#크롬 헤더임
h.putheader('Accept','text/html')
h.putheader('Referer','https://www.facebook.com/settings?tab=security&section=sessions&view')
h.putheader('Cookie',site_cookie)
h.endheaders()
errorCode, errorMessage, headers = h.getreply()
a = h.getfile()
text_tmp = a.read()
h.close()
