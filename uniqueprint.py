r=int(input())
list1=[int(x) for x in input().split()]
def Print(list1):
    final_list = []
    for num in range(len(list1)):
        i = num + 1
        for i in range(i, len(list1)):
            if list1[num]== list1[i]:
                final_list.append(list1[num])
    return final_list

k=Print(list1)
for i in range(len(list1)):
    if list1[i] not in k:
        print(list1[i])
