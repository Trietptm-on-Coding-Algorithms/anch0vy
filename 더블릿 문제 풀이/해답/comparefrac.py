a,b,c,d = map(float,raw_input().split())
if a/b > c/d:
    print 1
elif a/b == c/d:
    print 0
else:
    print -1
