a=int(input())
b=input().split()
l=[]
for i in range(a):
    l.append(int(b[i]))
s1=a//2
k=0
for i in range(s1):
    k=k+l[i]
a1=k//s1
s2=a-s1
k1=0
for i in range(s2):
    k1=k1+l[i]
a2=k1//s2
if(a1==a2):
    print('yes')
else:
    print('no')
