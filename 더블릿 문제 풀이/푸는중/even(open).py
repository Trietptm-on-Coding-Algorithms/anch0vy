a,b=map(int,raw_input().split())
import math
print int((b-math.floor(math.sqrt(b)))-(a-1-math.floor(math.sqrt(a-1))))
