a,b=input().split()
if(a.isdigit() and b.isdigit()):
    a=int(a)
    b=int(b)
    if(b==1):
      print("1 2")
    else:
       print("1 "+str(a-b))
 
