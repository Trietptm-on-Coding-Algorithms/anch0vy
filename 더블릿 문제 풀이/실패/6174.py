a=raw_input()
def b(c):
    d=[]
    print c
    for x in c:
        print x
        d+=[x]
    d.sort()
    t1=d
    d.sort(reverse=True)
    t2=d
    print id(t1),id(t2)
    return t1,t2
def c(a):
    return int(a[0])*1000+int(a[1])*100+int(a[2])*10+int(a[3])
n=0
t=''
while a is not '6174':
     t1,t2=b(a)
     print t1,t2
     a=str(c(t2)-c(t1))
     n+=1
print n
