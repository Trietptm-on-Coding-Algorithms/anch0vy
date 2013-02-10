a=float(input())
b=0
while 1:
    b=float(input())
    if b>998:
        print 'End of Output'
        exit()
    c=b-a
    print '%0.2f' %c
    a=b
