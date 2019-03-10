n = int(input())
chlsqrno = list(map(int, input().split(" ", n)))
day_month = list(map(int, input().split()))
d = int(day_month[0])
m = int(day_month[1])
count = 0
if m == 1:
    for item in chlsqrno:
        if item == d:
            count += 1
        else:
            pass

elif m > 1 or m <= 12:
    i = 0
    j = i + m
    while i < j & j <= n:
        temp = []
        for k in range(i, j):
            temp.append(chlsqrno[k])
        sum1 = sum(temp)
        if sum1 == d:
            count += 1
        i += 1
        j += 1
print(count)