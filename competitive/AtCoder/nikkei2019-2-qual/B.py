import math
N = int(input())
D = [int(x) for x in input().split()]

num = [0] * 100000

maxd = 0
for d in D:
    num[d] += 1
    maxd = max(d, maxd)

if D[0] != 0 or num[0] != 1:
    ans = 0
else:
    ans = 1
    for i in range(1, maxd):
        for _ in range(num[i+1]):
            ans *= num[i]%998244353
        ans %= 998244353
        if ans == 0:
            break
print(ans%998244353)
