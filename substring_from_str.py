string=input()
sub_string=input()
l=list(string)
ans=0
l1=[]
for i in range(len(l)):
  for j in range(i+1,len(l)+1):
    a=(l[i:j])
    b=''.join(a) 
    l1.append(b) 
for i in l1:
  if i==sub_string:
    ans+=1
    print(ans)
