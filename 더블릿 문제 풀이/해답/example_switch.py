a,b=map(int,raw_input().split())
c=0
q=[1,3,5,7,8,10,12]
if a%4==0:
    c=1
if q.count(b)==1:
    print 31
elif b==2:
    print 28+c
else:
    print 30
