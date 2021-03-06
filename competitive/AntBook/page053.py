import numpy as np

n = 4
weight = [2, 1, 3, 2]
value = [3, 2, 4, 2]
total_weight = 5

dp = np.ones((n+1, total_weight+1), np.int) * (-1)

def rec(i, remainning_weight):
    '''i番目以降の品物から重さの総和がj以下になるように再帰的に調べる'''
    if dp[i, remainning_weight] >= 0:
        return dp[i, remainning_weight]
    
    res = None
    if i == n:
        # 品物は n-1 番目までしかないので終わり。
        res = 0
    elif remainning_weight < weight[i]:
        # i番目は重すぎて入らないためi+1に行く
        res = rec(i+1, remainning_weight)
    else:
        # 入れない場合と入れる場合で良い方を採用
        res = max(rec(i+1, remainning_weight), rec(i+1, remainning_weight-weight[i]) + value[i])

    dp[i, remainning_weight] = res
    return res

print(rec(0, total_weight))
