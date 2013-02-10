# -*- coding: cp949 -*-
#python 3.2 ver
#소스코드 길이 줄여야 함.. ㅠㅠ 실패 ㅠㅠ
a,b = map(int,input().split())
c,d = map(int,input().split())
e=0
def z(a,b,c,d):
    return a/c + b/d
q=z(a,b,c,d)
w=z(c,a,d,b)
e=z(d,c,b,a)
r=z(b,d,a,c)
b=max(q,w,e,r)
if b==q:
    print(0)
elif b==w:
    print(1)
elif b==e:
    print(2)
elif b==r:
    print(3)
