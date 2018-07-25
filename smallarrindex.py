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
for i in range((e-1),f):
	min1=d[e-1]
	if(min1>d[i]):
		min1=d[i]
print(min1)
for i in range((g-1),h):
	min2=d[g-1]
	if(min2>d[i]):
		min2=d[i]
print(min2)
for i in range((k-1),j):
	min3=d[k-1]
	if(min3>d[i]):
		min3=d[i]
print(min3)
