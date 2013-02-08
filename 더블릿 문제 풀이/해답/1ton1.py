import sys
a=int(input())
z=sys.stdout.write
b=0
for x in range(1,a):
    z(str(x))
    z('+')
    b=b+x
z(str(a))
z('=')
z(str(b+a))
