r = int(input())
c = int(input())


def createsqrmatrix(r, c):
    list1 = []
    t = 1
    for i in range(r):
        temp = []
        for j in range(c):
            temp.append(t)
            t += 1
        list1.append(temp)
    return list1


mat = createsqrmatrix(r, c)


def printmat(mat):
    for i in range(r):
        temp = mat[i]
        for j in range(c):
            print(temp[j], end=" ")
        print()


print("INPUT")
printmat(mat)
