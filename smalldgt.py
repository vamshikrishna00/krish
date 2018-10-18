n=input()
k=int(input())
l=[]
for i in n:
	l.append(i)
l.sort()
g=len(l)-k
s=''
for i in range(g):
	s=s+l[i]
print(s)
