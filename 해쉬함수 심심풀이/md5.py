from __future__ import division
import hashlib



num = 340282366920938463463374607431768211456
n = 0
a = hashlib.md5('').hexdigest()
b = hashlib.md5(a).hexdigest()
while a != b:
    b = hashlib.md5(b).hexdigest()
    n = n + 1
    if n % 10000 == 0:
        print n,b,n/num*100
print a,b,n
