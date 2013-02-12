import math
b,c=map(float,input().split())
q=b**2-4*c
w=math.sqrt(q)
if q<0 or w.is_integer()==False:
    print('impossible')
else:
    z=(-b+w)/2
    x=(-b-w)/2
    print('(x'+str(int(z))+')(x'+str(int(x))+')')
