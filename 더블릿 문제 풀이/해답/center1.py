a=input()
b=0
c=0
for x in range(a):
    b=b+x+1
while c<b:
    c=c+a
    a+=1
if c==b:
    print 'O'
else:
    print 'X'
