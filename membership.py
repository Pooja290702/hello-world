a={1,2,3,4,5,6,7}
num=int(input())
found = False
if num in a:
    found=True

'''for i in a:
    if i==num:
        found=True
        break'''
if found:
    print('yes')
else:
    print('no')