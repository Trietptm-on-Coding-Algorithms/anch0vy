import numpy as np
import matplotlib
import matplotlib.pyplot as plt
f=open('test.log')
t=[]
v=[]
c=0
cc=0
for l in f:
	l=l.split(':')
	if l[0]=='INFO':
		c+=1
		tt,vv=l[2].split('\t')
		t.append(float(tt))
		v.append(float(vv))
		if float(vv)>1:
			cc+=1
plt.figure(figsize=(15,20),dpi=400)
plt.plot(t,v,'o')
tmp='%d / 20s'%c
tmp=tmp+'\nresponse time > 1s rate:%f%%'%(float(cc)/c*100)
plt.title(tmp)
plt.savefig('test.png')