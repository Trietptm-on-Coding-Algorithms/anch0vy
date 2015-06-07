import socket
import select
from hashlib import sha512
from prob import solve
def serve():
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(('',17884))
	s.listen(5)
	while 1:
		conn,addr = s.accept()
		print 'Connected by',addr
		data=conn.recv(10)
		print data
		#print solve(data)
		conn.sendall(solve(data))
		conn.close()

serve()