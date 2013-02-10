a,b = map(int,raw_input().split())
c=a/8
d=b/8
if a==c*8 and b==d*8:
    e=0
elif a==c*8:
    e=c
elif b==d*8:
    e=d
else:
    e=c+d-1
print 'The number of whole tiles is',str(c*d),'part tiles is',str(e)
