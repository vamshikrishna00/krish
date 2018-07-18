n=int(input())
a=input().split()
l=[]
for i in range(n):
    l.append(int(a[i]))
l.sort()
print(l[n-1])
