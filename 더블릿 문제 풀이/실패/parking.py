a=input()
q=raw_input().split()
b=[]
c=0
for x in q:
    b=b+[int(x)]
for x in b:
    c=c+x
c=float(c)/float(len(b))
c=int(c)
d=0
for x in b:
    print d
    d=d+abs(x-c)
print d
