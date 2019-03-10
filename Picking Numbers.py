from distlib.compat import raw_input

n = int(input())
array = [int(x) for x in raw_input().split()]
array = sorted(array)


def pickingNumber(array):
    count = 0
    i = 0
    while i < len(array):
        item = array[i]
        for j in range(i+1,len(array)):
            dif = abs(array[i] - array[j])
            if dif == 1:
                count += 1
            else:
                pass
        i += 1
    print(count)


pickingNumber(array)
