a,b=input().split()
a=int(a)
b=int(b)
c=input().split()
l=len(c)
d=[]
for i in range(l):
    d.append(c[i])
d.sort()
d=d[::-1]
print(d[b-1])
