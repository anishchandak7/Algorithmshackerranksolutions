l = []
l1 =list(map(int,input()))
    #n = int(input())
def sum(l1):
    for i in range(len(l1)):
        sum = 0
        sum = sum + l1[i]
        if sum > 0:
            l.append(l1[i])
        else:
            break
    for i in range(len(l)):
        print(l[i])

sum(l1)
