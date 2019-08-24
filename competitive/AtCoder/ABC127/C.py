'''久しぶりに累積和使った。解説読んだらmin max 使ってもっと簡単にやってた。'''
import numpy as np
N, M = [int(x) for x in input().split()]
ok = np.zeros(N+2, np.int64)

for _ in range(M):
  l, r = [int(x) for x in input().split()]
  ok[l] += 1
  ok[r+1] -= 1

cum = np.cumsum(ok)
print(np.sum(cum==M))
