a=raw_input().split()
for x in range(3):
    a[x]=int(a[x])
a.sort()
if a[2] < a[0]+a[1]:
    print 'yes'
else:
    print 'no'
