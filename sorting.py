import random


def comparelists(list1, list2):
    for item in list1:
        for item1 in list2:
            if item in list1 == item1 in list2:
                continue
        return True
    return False


n = int(input("enter the number of elements :"))
list_1 = []
for i in range(n):
    temp = int(input())
    list_1.append(temp)
print(list_1, end=" ")
list_2 = sorted(list_1, key=int)
print(list_2)
for x in range(n+1):
    i=random.randint(0,n)
    j=random.randint(0,n)
    if(i!=j):
        list_1[i],list_1[j]=list_1[j],list_1[i]
        if not comparelists(list_1, list_2):
            continue
        else:
            print(list_1)
