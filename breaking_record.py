n=int(input())
score=list(map(int,input().split(" ",n)))

def count_minmax(score):
    temp = []
    count_min = 0
    count_max = 0

    min = score[0]
    max = score[0]

    for i in range(1, len(score)):
        if score[i] < min:
            min = score[i]
            count_min += 1
        elif (score[i] > max):
            max = score[i]
            count_max += 1
        elif (score[i] == min or score[i] == max):
            pass

    temp.append(count_max)
    temp.append(count_min)
    return temp


min_max = count_minmax(score)

for i in range(len(min_max)):
    print(min_max[i],end=" ")
