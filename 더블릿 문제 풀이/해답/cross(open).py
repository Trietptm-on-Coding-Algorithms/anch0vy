a,b=map(int,raw_input().split())
c,d=map(int,raw_input().split())
z=min(a,b)
x=max(a,b)
q=(z<c<x)^(z<d<x)
if q:
    print 'cross'
else:
    print 'not cross'
