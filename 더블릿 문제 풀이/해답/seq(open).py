a,b = map(int,raw_input().split())
if a>b:
    a,b = b,a
for x in range(a,b+1):
    print x,
