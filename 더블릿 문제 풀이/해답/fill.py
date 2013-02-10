a,b,c=raw_input().split()
a=float(a)
b=int(b)
c=int(c)
d=0
if a<=4.5 and b>=150 and c>=200:
    print 'Wide Receiver',
    d=1
if a<=6.0 and b>=300 and c>=500:
    print 'Lineman',
    d=1
if a<=5.0 and b>=200 and c>=300:
    print 'Quarterback',
    d=1
if d is not 1:
    print 'No positions'
