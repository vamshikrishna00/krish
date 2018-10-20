a=input()
k=0
v=['a','e','i','o','u','A','E','I','O','U']
for i in a:
    if i in v:
        k=1
if k==1:
    print('yes')
else:
    print('no')
