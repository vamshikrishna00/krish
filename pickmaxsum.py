# your code
a=int(input())
b=input().split()
l= []
for i in range(a):
    l.append(int(b[i]))
c= 0
c1=0
s1=0
s2=0
k=[]
k1=[]
for i in l:
    if(c%2==1):
        k.append(i)
    c+= 1
for i in l:
    if c1%2!=1:
        k1.append(i)
    c1+=1
for i in k:
    s2= s2+i
for i in k1:
    s1=s1+i
if(s1>s2):
    print(s1)
else:
    print(s2)
