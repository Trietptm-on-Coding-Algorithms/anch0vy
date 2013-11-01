# -*- coding: cp949 -*-
from socket import *
import re
import pprint
import copy
import time

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.93.128',5180))
test1,addr=clientsock.recvfrom(1024)#round
clientsock.send('105/116/99/100/56/25')
test1,addr=clientsock.recvfrom(1024)#round
clientsock.send('102/100/13')
test1,addr=clientsock.recvfrom(1024)#round
clientsock.send('102/100/13')
test1,addr=clientsock.recvfrom(1024)#round
clientsock.send('102/100/13')
test1,addr=clientsock.recvfrom(1024)#round
clientsock.send('102/100/13')
test1,addr=clientsock.recvfrom(1024)#round

clientsock.close()
    
