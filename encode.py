new =input('')
p=""
for c in new:
    if ord(c)<=87:
        p+= chr(ord(c) + 3)
    else:
        k=90-ord(c)
        n=chr(67-k)
        p+=n
        
print(p)
