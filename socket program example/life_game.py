# -*- coding: cp949 -*-
from socket import *
import re
import pprint
import copy
import time

cs = socket(AF_INET, SOCK_STREAM)
cs.connect(('210.126.48.194',34567))
a,b=cs.recvfrom(2048)
print a
cs.send('get')
a,b= cs.recvfrom(2048)
print a
cs.send('../')
a,b= cs.recvfrom(2048)
print a,'1'
cs.send('')
a,b= cs.recvfrom(2048)
print a,'2'
a,b= cs.recvfrom(2048)
print a
a,b= cs.recvfrom(2048)
print a
'''
test1,addr=clientsock.recvfrom(1024)#round
clientsock.send('105/116/99/100/56/25')
'''
cs.close()
    
