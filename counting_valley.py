# * A mountain is a sequence of consecutive steps above sea level,
# starting with a step up from sea level and ending with a step down to sea level.
# * A valley is a sequence of consecutive steps below sea level, starting with a step
# down from sea level and ending with a step up to sea level.

n = int(input())
steps = list(map(str,input().split()))
def countvalley(steps):
    valley = 0
    for i in range(len(steps)):
        for j in range(i+1,len(steps)+1):
            if steps[i] == 'D':
                if steps[j] == 'D':
                    valley += 1
                elif steps[j] == 'U':
                    continue
            elif steps[i] == 'U':
                continue
    return valley


result = countvalley(steps)
print(result)