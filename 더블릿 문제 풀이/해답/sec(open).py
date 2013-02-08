a=int(raw_input())
b=a/86400
a=a-b*86400
c=a/3600
a=a-c*3600
d=a/60
a=a-d*60
print b,c,d,a
