x=int(input())
y=int(input())
def lcm(x,y):
    if x > y:
       greater = x
    else:
       greater = y

    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

    return lcm
print(lcm(x,y))
