s=input()
b=len(s)
l=list(s)
s=''
if b%2!=0:
    for i in range(b//2):
        s=s+l[i]
    s+='*'
    j=(b//2)+1
else:
    for i in range((b//2)-1):
        s=s+l[i]
    s+='*'
    j=(b//2)+1
for i in range(j,b):
    s+=l[i]
print(s)
