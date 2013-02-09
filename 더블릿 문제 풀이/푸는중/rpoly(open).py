a,b = map(float,raw_input().split())
import math
c=2.0/b*math.pi
d=a*a*math.sin(c)/2.0*b
print '%0.3f' %d
