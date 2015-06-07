# -*- coding: cp949 -*-
import sqlite3
import time
db=sqlite3.connect('''d:\History Index 2013-09''')
tmp=db.execute('select * from info;')
tmp=tmp.fetchall()
info=[]
for x in tmp:
    t=x[0]/1000000 - 11644441200
    info = info + [t]
info.sort()
print time.ctime(info[0])
print time.ctime(info[-1])

h1=0
h2=0
h3=0
h4=0
h5=0
h6=0
s=0
for x in range(len(info)-1):
    q=info[x+1]-info[x]
    if q<60*20:
        pass
    elif q<60*60:
        s=s+1
    elif q<60*60*2:
        h1=h1+1
    elif q<60*60*3:
        h2=h2+1
    elif q<60*60*4:
        h3=h3+1
    elif q<60*60*5:
        h4=h4+1
    elif q<60*60*6:
        h5=h5+1
print len(info),s
print '1시간~2시간:',h1
print '2시간~3시간:',h2
print '3시간~4시간:',h3
print '4시간~5시간:',h4
print '5시간~6시간:',h5
