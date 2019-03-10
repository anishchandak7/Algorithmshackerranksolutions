from itertools import combinations
nk = list(map(int,input().split()))
n=nk[0]
k=nk[1]
a = list(map(int, input().split()))
print(sum(sum(pair) % k == 0 for pair in combinations(a, 2)))