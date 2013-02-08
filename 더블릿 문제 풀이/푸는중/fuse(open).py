import math
a,b,c = map(float,raw_input().split())
d = (a*2.5 + b*2.0 + c*0.5)*2
print int(math.ceil(d/10)*10),
print 'amperes'
