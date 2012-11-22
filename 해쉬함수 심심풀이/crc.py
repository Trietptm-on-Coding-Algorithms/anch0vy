from __future__ import division
import zlib
num = 16 ** 8
def crc(prev):
    prev = zlib.crc32(prev, 0)
    return "%X"%(prev & 0xFFFFFFFF)
a = crc('test')
b = crc(a)
n = 0
while a != b:
    b = crc(b)
    n = n + 1
    if n % 100000 == 0:
        print n,a,b,n/num*100,'%'
print '#############################################'
print n,a,b
print '#############################################'
