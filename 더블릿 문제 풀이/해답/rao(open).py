a,b,c = map(int,raw_input().split())
d=[a,b,c]
d.sort()
e=d[2]**2-d[1]**2-d[0]**2
if e>0:
    print 'obtuse'
elif e<0:
    print 'acute'
else:
    print 'right'
