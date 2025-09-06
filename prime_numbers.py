def prime(a):
    if a==0 or a==1 :
       return False
    if a==2:
        return True
    if a%2==0:
        return False
    for i in range(3,1+int(a**0.5),2):
        if a%i==0:
            return False
    return True
a=int(input())
if prime(a):
    print(a,' is prime')
else:
    print(a, ' is not prime')
