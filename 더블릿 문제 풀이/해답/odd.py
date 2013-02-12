a=[input(),input(),input(),input(),input(),input(),input()]
b=0
c=[]
for x in a:
    if x%2==1:
        b=b+x
        c=c+[x]
if b==0:
    print -1
else:
    print b
    print min(c)
