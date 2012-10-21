import os
import sys
import hashlib

def hashing_list(h_list):
    new = ''
    n = 0
    for text in h_list:
        if text is not '':
            q = hashlib.md5(text).hexdigest()
            if n % 20 == 0:
                print float(n)/float(len(h_list))*100,q
            new = new[:] + q[0:2]
        n = n+1
    return new

def hashing_str(text):
    new = ''
    for t in range(0,len(text),32*2):
        new = new[:] + hashlib.md5(text[t:t+32*2]).hexdigest()
    print 'hashing_str', new
    return new

diff_1 = sys.argv[1]
diff_2 = sys.argv[2]

diff_1 = open(diff_1,'rb').read()
diff_2 = open(diff_2,'rb').read()

diff_1 = diff_1.split('\000')
diff_2 = diff_2.split('\000')

#if len(diff_1)is not len(diff_2):
#    if len(diff_1) > len(diff_2):
#        num = 0
#        while num < (len(diff_1) - len(diff_2)):
#            diff_2.append('padding')
#        print len(diff_1),len(diff_2)
#    if len(diff_2) > len(diff_1):
#        num = 0
#        while num < (len(diff_2) - len(diff_1)):
#            diff_1.append('padding')
#        print len(diff_1),len(diff_2)

diff_1 = hashing_list(diff_1)
diff_2 = hashing_list(diff_2)
print '1',diff_1
print '2',diff_2

