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

_base_time=time.time()

def multi():
	NUM=100
	ps=[Process(target=connect,args=(logging,_answer,_base_time)) for x in xrange(NUM)]
	for p in ps:
		p.start()
	time.sleep(20)
	print 'end'
	for p in ps:
		p.terminate()
	sys.exit()

def connect(log,answer,base_time):
	while 1:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(10)#timeout: 10sec
		try:
			rand=random.randint(0,1000)
			t=time.time()
			s.connect((IP,17884))#19940828%65536
			s.sendall(str(rand))
			res=s.recv(6400*4)#len(answer[0])==6400
			t=time.time()-t
			if answer[rand]!=res:
				log.error('[!]get wrong answer!')
			else:
				log.info(repr(time.time()-base_time)+'\t'+repr(t))
		except socket.timeout:
			log.info(repr(time.time()-base_time)+'\t'+repr(10.0))
		except IndexError:
			print 'randerror:',rand
		except Exception,e:
			log.error('[!]error:',exc_info=True)
	

def make_answer_list():
	print '[*]start prob-answer list...'
	t=time.time()
	for n in xrange(1010):
		ans=solve(str(n))
		_answer.append(ans)
	print '[*]end',time.time()-t


if __name__=='__main__':
	make_answer_list()
	logging.basicConfig(filename='./test.log',level=logging.DEBUG)
	multi()