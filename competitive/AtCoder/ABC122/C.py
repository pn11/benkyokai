'''アルゴリズムは簡単だけどPythonだと累積和使ってもぎりぎり'''
import numpy as np
def find_AC(S):
  ret = [0]*len(S)
  for i in range(len(S)-1):
    if S[i] == 'A' and S[i+1] == 'C':
      ret[i+1] = 1
  return ret

N, Q = [int(x) for x in input().split()]
S = input()

cum = np.cumsum(find_AC(S))

for _ in range(Q):
  l, r = [int(x) for x in input().split()]
  ans = cum[r-1] - cum[l-1]
  print(ans)
