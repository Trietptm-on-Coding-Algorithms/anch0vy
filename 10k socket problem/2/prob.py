from hashlib import sha512
import time
answer=[]

def solve(s):
	r=''
	for n in xrange(300):
		s=sha512(s).digest()
		r=r+s
	return r


def _make_answer_list():
	print '[*]start prob-answer list...'
	t=time.time()
	for n in xrange(1000):
		ans=sha512(str(n)).digest()
		for x in xrange(100-1):
			tmp=sha512(ans).digest()
			ans=ans+tmp
		answer.append(ans)
	print '[*]end',time.time()-t



if __name__=='__main__':
	make_answer_list()
	print solve('2').encode('hex')[:500]
	print answer[2].encode('hex')[:500]
	print 
	print solve('2').encode('hex')[-100:]
	print answer[2].encode('hex')[-100:]
	print 
	print len(solve('2'))
	print len(answer[2])
	print
	print solve('2')==answer[2]