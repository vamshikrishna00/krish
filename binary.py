a=int(input())
b=input().split()
c=[]
for i in range(a):
	c.append(b[i])
c.sort(reverse=True)
for i in c:
	print(i)
