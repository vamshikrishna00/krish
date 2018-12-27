x,y=input().split()
count=0
x=set(x)
y=set(y)
for i in x:
    if i in y:
        count=count+1
if(count>=2):
    print('yes')
elif(count<2):
    print('no')
