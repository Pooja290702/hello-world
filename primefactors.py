def primes(a):
    count=0
    if a==0 or a==1:
        count=2
    elif a==2:
        count=1
    for i in range(1,a//2+1):
        if a%i==0:
            count+=1
    return count==1
a=int(input())
l=[]
for i in range(1,a//2+1):
    s=primes(i)
    if s==True:
        if a%i==0:
            l.append(i)
            a=a//i
if a>1:
    for i in range(a):
        for j in l:
            if a%j==0:
                l.append(j)
                a=a/j
l.sort()
print(l)
