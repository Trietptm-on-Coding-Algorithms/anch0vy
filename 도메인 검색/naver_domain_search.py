# -*- coding: cp949 -*-
import re
import urllib
import time

f=raw_input('file path:')
f=open(f,'w')
api='http://api.arzz.com/google/?'
keyword='site:naver.com filetype:jpg'
f.write(keyword)
f.write('\n')
page=1
listnum=50
site=''
name=[]
dic={}
num=0
key_num=0
for x in range(1000):
    url=api+'keyword='+keyword+'&page='+str(page)+'&listnum='+str(listnum)+'&site='+site
    print url
    q=urllib.urlopen(url)
    q=q.read()
    q = re.findall('url":"http:\\\\/\\\\/?(.*?)\\\\',q,re.DOTALL)
    print 'url num:',len(q)
    if len(q) == 0:
        f.close()
        raw_input('end')
    for x in q:
        x=x.replace('\\/','\\')
        if name.count(x)==0:
            name=name+[x]
            dic[x]=1
            f.write(x)
            f.write('\n')
            f.flush()
            num=num+1
        else:
            if dic[x] == -1:
                pass
            else:
                dic[x]=dic[x]+1
    print 'added:',num
    if num < 2 :
        print 'url_list:',q
        print 'dic:',dic
    num=0
    check=1
    while check:
        dic_value=dic.values()
        dic_key=dic.keys()
        dic_item=dic.items()
        value_max=max(dic_value)
        if value_max > 10:
            index=dic_value.index(value_max)
            key=dic_item[index][0]
            if key_num<25:
                keyword = keyword + ' -' + key
                page=page-1
            dic[key]=-1
            print 'block key:',key
        else:
            check = 0
    page=page+1
    print 'stop...',
    time.sleep(30)
    print 'resume'
f.close()
