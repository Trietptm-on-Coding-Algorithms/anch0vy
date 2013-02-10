a,b = map(int,raw_input().split())
if (a-b)/2 < 0 or (a-b)%2==1:
    print 'impossible'
else:
    print (a+b)/2,(a-b)/2
