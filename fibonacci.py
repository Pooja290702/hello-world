n=int(input())
if n==0:
    print([])
elif n==1:
    print([0])
else: 
    l=[0,1]

    for i in range(2,n):
        l.append(l[i-2]+l[i-1])
    print(l)
    
