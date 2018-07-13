i=int(input())
string = input("")
newstr = string

vowels = ('a', 'e', 'i', 'o', 'u')
for x in string.lower():
    if x in vowels:
        newstr = newstr.replace(x,"")
    
print(newstr[::-1])
