a,b=input().split()
a=int(a)
b=int(b)
c=input().split()
d=[]
for i in range(a):
	d.append(int(c[i]))
e,f=input().split()
g,h=input().split()
k,j=input().split()
e=int(e)
f=int(f)
g=int(g)
h=int(h)
k=int(k)
j=int(j)
s=0
for i in range(e-1,f):
	s=s+d[i]
print(s)
s=0
for i in range(g-1,h):
	s=s+d[i]
print(s)
s=0
for i in range(k-1,j):
	s=s+d[i]
print(s)
