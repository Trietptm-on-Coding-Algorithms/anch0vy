# -*- coding: cp949 -*-
import hashlib
import time
import sys
import os

def remove_null(_list):
    n = _list.count('\x00')
    for in range(0,n):
        _list.remove('\x00')
    return _list

def hashing_list(_list):
    result = ''
    for s in 
    

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

diff_1 = diff_1.split('\x00')
diff_2 = diff_2.split('\x00')

diff_1 = remove_null(diff_1)
diff_2 = remove_null(diff_2)
