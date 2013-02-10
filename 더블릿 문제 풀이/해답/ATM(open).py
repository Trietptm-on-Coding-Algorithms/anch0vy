a,b = map(float,raw_input().split())
a=int(a)
if a%5:
    print '%0.2f' %b
else:
    c=a/5
    d=b-float(c)*5.0-0.5
    if d<0:
        print b
    else:
        print '%0.2f' %d
