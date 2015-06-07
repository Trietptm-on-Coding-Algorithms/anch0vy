import socket
import random
import time
import sys
import logging
import multiprocessing
from multiprocessing import Process,Queue
from hashlib import sha512
from prob import solve

_answer=[]
IP='127.0.0.1'
NUM=1000


def connect(answer,start_q):
	log=logging
	logging.basicConfig(filename='./test.log',level=logging.DEBUG)
	base_time=time.time()
	while 1:
		if start_q.qsize()==NUM:
			break
		else:
			time.sleep(1)
	while time.time()-base_time<20.0:
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
		except socket.timeout,socket.error:
			log.info(repr(time.time()-base_time)+'\t'+repr(10.0))
		except IndexError:
			print 'randerror:',rand
		except Exception,e:
			log.error('[!]error:',exc_info=True)



if __name__=='__main__':
	def make_answer_list():
		print '[*]start prob-answer list...'
		t=time.time()
		for n in xrange(1010):
			ans=solve(str(n))
			_answer.append(ans)
		print '[*]end',time.time()-t

	def multi():
		start_q=Queue()
		n=0
		ps=[Process(target=connect,args=(_answer,start_q)) for x in xrange(NUM)]
		for p in ps:
			p.start()
			start_q.put(1)
			n+=1
			print '[!]start %d proc'%n
	logging.basicConfig(filename='./test.log',level=logging.DEBUG)
	make_answer_list()
	multi()
	print 'end'