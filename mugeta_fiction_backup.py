# -*- coding: utf-8 -*-
#변수
#이동할 페이지 주소 next_page
#본문저장변수 // text_main
#저장  text_save
#임시 html text_tmp
#소설명 text_name
#페이지 text_page
#정규식 p
#현페이지 n

import httplib
import urllib
import re
import string

#소설시작주소 >next_page
#소설장수 >text_page
#소설명 >text_name
#쿠키값 > site_coolie

n = 1
text_name = raw_input('what is name of book? ')
text_page = raw_input('how many pages? ')
next_page = raw_input('what is start url? ')
#사이트 쿠키값 내껄로 고정
site_cookie = 'user_no=oGRl9GlKl0Z5eqikoJ2bSSlkaoLZKHmPieLjlcSi3Jm'
text_save = file(text_name,'w')
text_save.write(''.join('MUGETA novel -> txt file program\nThis program was made by WH for YOU\nMakeperson\'s blog\n========================\nblog.naver.com/aaaa875\n========================\n '))
text_save.close()
n = 1

while int(n)<=int(text_page):
	print n,'page\n'
        host = 'wr.mugeta.com'
        h = httplib.HTTP(host)
	h.putrequest('GET','/?PAGEKEY='+next_page)
	h.putheader('Host', host)
	h.putheader('User-Agent', 'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3') 	
	h.putheader('Accept','text/html')
	h.putheader('Cookie',site_cookie)
	h.endheaders()
	errorCode, errorMessage, headers = h.getreply()
    	a = h.getfile()
    	text_tmp = a.read()
    	h.close()
	#//정규식_본문_1차
    	tmp_a = ''.join(re.findall('"90%" align="center" ?(.*?)</td>',text_tmp,re.DOTALL))
        print '================='
	#//정규식_본문_2차 쓸데없는것 제거&변환
        text_main=str(re.sub('&#39;','\'',tmp_a,1000,re.DOTALL))
        text_main=str(re.sub('<br>','\n',text_main,1000,re.DOTALL))
        text_main=str(re.sub('&quot;','"',text_main,1000,re.DOTALL))
        text_main=str(re.sub('','',text_main,1000,re.DOTALL))
        text_main=str(re.sub('	','',text_main,1000,re.DOTALL))
        text_main=str(re.sub('<tr>','',text_main,1000,re.DOTALL))
        text_main=str(re.sub('<td>','',text_main,1000,re.DOTALL))
        text_main=str(re.sub('<tr>','',text_main,1000,re.DOTALL))

	#//텍스트에 저장
	text_save = file(text_name,'a+')
	text_save.write(text_main)
	text_save.close()

	#//다음페이지 주소 추출
	m = re.findall('<a href=[\'](.*?)[\']',text_tmp,re.DOTALL)
	next_page = m[1]
	next_page = ''.join(next_page)
	n = n+1
print text_name
text_save = file(text_name,'a+')
text_save.write(''.join('\n\nMUGETA novel -> txt file program\nThis program was made by WH for YOU\nMakeperson\'s blog\n========================\nblog.naver.com/aaaa875\n========================\n '))
text_save.close()
print 'complete'