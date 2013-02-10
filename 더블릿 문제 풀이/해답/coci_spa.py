a,b = map(int,raw_input().split())
b = b - 45
if b<0:
    a=a-1
    b=b+60
if a<0:
    a=a+24
print a,b
