import numpy as np

n = 4
weight = [2, 1, 3, 2]
value = [3, 2, 4, 2]
total_weight = 5

dp = np.zeros((n+1, total_weight+1), np.int)


def solve():
    for i in range(n-1, -1, -1):
        for j in range(0, total_weight+1):
            if j < weight[i]:
                dp[i, j] = dp[i+1][j]
            else:
                dp[i, j] = max(dp[i+1][j], dp[i+1][j-weight[i]]+value[i])
    print(dp[0, total_weight])

solve()
