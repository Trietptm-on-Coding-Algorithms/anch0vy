#python 3.2 ver
a=int(input())
a=str(bin(a))[2:]
for x in range(len(a),0,-1):
    if a[x-1]=='1':
        print(len(a)-x,end=' ')
