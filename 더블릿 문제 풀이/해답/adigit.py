a,b,c,d,e,f,g = map(int,raw_input().split())
x = [a,b,c,d,e,f,g]
a1,a2,a3=0,0,0
for y in x:
    if len(str(y)) == 1:
        a1+=y
    elif len(str(y)) == 2:
        a2+=y
    else:
        a3+=y
print a1,a2,a3
        
