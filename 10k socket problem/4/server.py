import socket
import select
import time
from hashlib import sha512
from prob import solve
def serve():
	while 1:
		time.sleep(0.1)
		try:
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.bind(('',17884))
			s.listen(1500)
			print '[*]make SOCK_STREAM'
			while 1:
				conn,addr = s.accept()
				print 'Connected by',addr
				data=conn.recv(10)
				print data
				#print solve(data)
				conn.sendall(solve(data))
				conn.close()
		except socket.error,e:
			print '[!]error:',
			print e
			s.close()
			pass

serve()