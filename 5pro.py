x,y,z=input().split()
x=int(x)
y=int(y)
z=int(z)
sum=0
p=0
for i in range(0,x):
    if(x%2==0):
        sum=sum+y+z
        if(x==sum):
            p=sum
            break
if(p==x):
    print("YES")
else:
    print("NO")
