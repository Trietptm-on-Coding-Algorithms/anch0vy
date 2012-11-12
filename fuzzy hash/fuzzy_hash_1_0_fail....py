# -*- coding: cp949 -*-
from __future__ import division
import hashlib
import time
import sys
import os

def remove_null(_list):
    n = _list.count('')
    for a in range(0,n):
        _list.remove('')
    return _list

def hashing_list(_list):
    result = ''
    n = 0
    size = 0
    m = 0
    for s in _list:
        result = result + hashlib.md5(s).hexdigest()[:3]
        n = n + 1
        #if not n%3000:
            #print n
        if len(s) > 800:
            size = size + len(s)
            m = m + 1
    print size/m , m , n
    return result

def diffing(list_1,list_2,max_count): #망함
    r_list_1 = ''
    r_list_2 = ''
    for n in range(0,len(list_1)-3,3): #n은 그냥 반복을 위해서...
        print n#debug
        for m in range(0,max_count*3-3,3):
            if list_1[0:3] == list_2[m:m+3]:
                r_list_1 = r_list_1 + 'x'*len(list_2[0:m]) + list_1[m:m+3]
                r_list_2 = r_list_2 + list_2[0:m+3]
                list_1 = list_1[3:]
                list_2 = list_2[m+3:]
            if m == max_count*3-3:
                r_list_1 = r_list_1 + list_1[0:3]
                r_list_2 = r_list_2 + 'x'*len(list_1[0:3]) + list_2[m:m+3]
                list_1 = list_1[m+3:]
                list_2 - list_2[3:]
    for n in range(0,len(r_list_1)-10,10): #debug
        print r_list_1[n:n+10]
        print r_list_2[n:n+10]
        raw_input('asdf')#debug
    return r_list_1,r_list_2
    

try:
    sys.argv[1] #꼼수
    sys.argv[2]
except:
    print '사용법: 프로그램명 비교1 비교2'
    exit(-1)
try:
    f_diff_1 = open(sys.argv[1],'rb')
    f_diff_2 = open(sys.argv[2],'rb')
except IOError:
    print 'no such file'
    exit(-1)

diff_1 = f_diff_1.read()
diff_2 = f_diff_2.read()

f_diff_1.close()
f_diff_2.close()
print 'start split by null'
diff_1 = diff_1.split('\x00')
diff_2 = diff_2.split('\x00')
print 'start remove empty member'
diff_1 = remove_null(diff_1)
diff_2 = remove_null(diff_2)
print 'start hashing...'
diff_1 = hashing_list(diff_1)
diff_2 = hashing_list(diff_2)
if diff_1 == diff_2:
    print 'equal!!'
    #exit(0)
print 'start diff'
#diff_1,diff_2 = diffing(diff_1,diff_2,10)

#raw_input('end')
print diff_1
print diff_2
