# -*- coding: cp949 -*-
#소스 줄여보자
a=[]
b=0
for x in range(12):
    a=a+[input()]
for x in a:
    b=b+x
c=int(b/12)
d=round(b/12-c,2)
print '$'+str(c)+str(d)[1:]
