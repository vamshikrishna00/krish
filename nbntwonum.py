a=int(input())
b,c=input().split()
b=int(b)
c=int(c)
k=0
if a>b:
    if a<c:
        k=1
if k==1:
    print('yes')
else:
    print('no')
