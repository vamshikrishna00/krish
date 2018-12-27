z=int(input())
count=0
count1=0
w=0
e=0
for i in range(z):
    x=input().split()
    break
if(z>=2 and z<100000):
    if(z%2==0):
        q=z//2
        for j in range(q):
            w=w+int(x[j])
            count+=1
        for k in range(q,z):
            e=e+int(x[k])
            count1+=1
    else:
        t=z//2+1
        for j in range(t):
            w=w+int(x[j])
            count+=1
        for k in range(t,z):
            e=e+int(x[k])
            count1+=1
    if(w//count==e//count1):
        print('yes')
    else:
        print('no')
else:
    print('no')
