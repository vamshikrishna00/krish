c,d=input().split()
c=int(c)
d=int(d)
q=[]
w=[]
for i in range(c):
    x=input().split()
    break
for j in range(0,d):
    u,v=input().split()
    u=int(u)
    v=int(v)
    q.append(u)
    w.append(v)
for k in range(0,d):
    t=q[k]
    g=w[k]
    z=0
    for l in range(t,g+1):
        z=z^int(x[l-1])
    print(z)
