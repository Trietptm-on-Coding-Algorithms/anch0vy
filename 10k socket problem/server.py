'''
ulimit -Sn 2000
'''
#from gevent.monkey import patch_all
import socket
import select
import time
from multiprocessing import Process,Queue
from hashlib import sha512
from prob import solve
#patch_all()#wow
print '[*]monkey magic'
NUM=4
def get_part():
	#get conn and put it to queue
	while 1:
		time.sleep(0.1)
		try:
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.bind(('',17884))
			s.listen(10000)
			print '[*]make SOCK_STREAM'
			while 1:
				conn,_ = s.accept()
				p=Process(target=send_part,args=(conn,))
				p.start()
		except Exception,e:
			print '[!]error:',
			print e
			pass

def send_part(conn):
	try:
		#print 'Connected by',addr
		data=conn.recv(10)
		conn.sendall(solve(data))
		conn.close()
	except socket.error,e:
		print '[!]error:',e
	finally:
		conn.close()

def lobby():
	get_part()

lobby()