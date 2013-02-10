a,b,c,d = map(float,raw_input().split())
if a==c:
    if b==d:
        print 'many'
    else:
        print 'none'
else:
    e=(d-b)/(a-c)
    print '%0.3f'%e
