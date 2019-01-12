a,b=input().split()
c=input().split()
d=input().split()
a=int(a)
b=int(b)
e=[]
f=[]
for i in range(a):
    e.append(int(c[i]))
for i in range(b):
    f.append(int(d[i]))
for i in range(len(f)):
    e.append(f[i])
    x=sorted(e)
    print(max(x),end=' ')
