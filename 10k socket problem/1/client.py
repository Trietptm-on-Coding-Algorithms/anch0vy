import socket
import random
import time
import sys
import logging
from multiprocessing import Process,Queue
from hashlib import sha512
from prob import solve


_answer=[]
IP='127.0.0.1'


def multi():
	ps=[Process(target=connect,args=(logging,_answer)) for x in xrange(10)]
	for p in ps:
		p.start()


	


def connect(log,answer,):
	while 1:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(10)#timeout: 10sec
		try:
			rand=random.randint(0,1000)
			t=time.time()
			s.connect((IP,17884))#19940828%65536
			s.sendall(str(rand))
			res=s.recv(7000)#len(answer[0])==6400
			t=time.time()-t
			if answer[rand]!=res:
				log.error('[!]get wrong answer!')
			else:
				log.info(repr(time.time())+'\t'+repr(t))
		except socket.timeout:
			log.info('timeout')
		except Exception,e:
			log.error('[!]error:',exc_info=True)
	

def make_answer_list():
	print '[*]start prob-answer list...'
	t=time.time()
	for n in xrange(1000):
		ans=solve(str(n))
		_answer.append(ans)
	print '[*]end',time.time()-t


if __name__=='__main__':
	make_answer_list()
	logging.basicConfig(filename='./test.log',level=logging.DEBUG)
	multi()
	#print connect(logging,_answer)
