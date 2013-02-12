a=input()
b=0
c=0
d=1
for x in range(1,a+1):
    if a%x==0:
        b=b+1
        c=c+x
        d=d*x
        print x,
print '\n',
print b
print c
print str(d)[-1]
