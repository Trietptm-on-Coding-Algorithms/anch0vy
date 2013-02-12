a,b=map(int,raw_input().split())
print a,b,
while a-b>=0:
    print a-b,  
    c=a
    a=b
    b=c-b
