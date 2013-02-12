p=raw_input
i=int
a,b=map(i,p().split())
c,d=map(i,p().split())
e,f=map(i,p().split())
def z(a):
 if a.count(a[0]) is 1:
  print a[0],
 elif a.count(a[1]) is 1:
  print a[1],
 else:
  print a[2],
q=[a,c,e]
w=[b,d,f]
z(q)
z(w)
