a=raw_input().split()
a=a[:-1]
b=''
n=0
for x in a:
    if b is not x:
        if n is not 0:
            print n,b,
        b=x
        n=0
    else:
        n+=1
print n,b,
