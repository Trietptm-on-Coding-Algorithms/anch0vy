a,b=map(int,raw_input().split())
if a is 0:
    print a,'!|',b
    exit()
if b%a==0:
    print a,'|',b
else:
    print a,'!|',b
