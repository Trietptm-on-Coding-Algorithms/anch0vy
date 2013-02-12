a,b,c=map(int,raw_input().split())
q=[a,b,c]
d=0
for x in range(2):
    if d<abs(q[x]-q[x+1]):
        d=abs(q[x]-q[x+1])
print d-1
