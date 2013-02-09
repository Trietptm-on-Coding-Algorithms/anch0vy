a,b = map(int,raw_input().split())
import sys
z=sys.stdout.write
def q(w):
    if w%2==1:
        z('odd')
    else:
        z('even')
q(a)
z('+')
q(b)
z('=')
q(a+b)
z('\n')
q(a)
z('*')
q(b)
z('=')
q(a*b)
z('\n')
