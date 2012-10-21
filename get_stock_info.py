# -*- coding: cp949 -*-

import urllib
import re
import os

def parsing(a,b,c,d,e):
    print 'start parsing:' + d
    f = open(e+'\\stock_'+a+'_'+b+'_'+c+'.txt' ,'w')
    get_url = 'http://www.krx.co.kr/por_kor/corelogic/process/sto/stc_d_011.xhtml?data-only=true&isu_cd='+ a +'&fr_work_dt=' + b + '&to_work_dt=' + c
    data = urllib.urlopen(get_url).read()
    data = data.replace('</td></tr>','\n')
    data = data.replace('<tr><td>','')
    data = data.replace('<img src="http://inc.krx.co.kr/image/cm/icon/i401.gif" alt = "\xec\x83\x81\xec\x8a\xb9"/>','') #상승
    data = data.replace('<img src="http://inc.krx.co.kr/image/cm/icon/i402.gif" alt = "\xed\x95\x98\xeb\x9d\xbd"/>','') #하락
#없는 데이터    data = data.replace('<img src="http://inc.krx.co.kr/image/cm/icon/i403.gif" alt = ""/>','')
    data = data.replace('<img src="http://inc.krx.co.kr/image/cm/icon/i404.gif" alt = "\xec\x83\x81\xed\x95\x9c"/>','') #상한
    data = data.replace('<img src="http://inc.krx.co.kr/image/cm/icon/i405.gif" alt = "\xed\x95\x98\xed\x95\x9c"/>','') #하한
    data = data.replace('<em class ="up">','')
    data = data.replace('<em class ="down">','')
    data = data.replace(',','')
    data = data.replace('</td><td>',',')
    data = data.replace('</em>','')
    data = data.replace(' ','')
    f.write(data)
    f.close()


start_date = str(raw_input('start date: '))
end_date = str(raw_input('end date: '))
stock_list = str(raw_input('stock list: '))
folder = str(raw_input('folder: '))

f = open(stock_list,'r')
while 1:
    line = f.readline()
    if not line:
        break
    stock_info = line.split(',')
    stock_name, stock_id = stock_info
    stock_id = stock_id.replace('\n','')
    parsing(stock_id,start_date,end_date,stock_name,folder)
