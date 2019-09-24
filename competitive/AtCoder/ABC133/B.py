import numpy as np

N, D = [int(x) for x in input().split()]

X = np.zeros((N, D), np.float)
for i in range(N):
  X[i,] = [int(x) for x in input().split()]

def dist(X1, X2):
  return np.linalg.norm(X1-X2)

ans = 0
for i in range(N-1):
  for j in range(i+1, N):
    d = dist(X[i,], X[j,])
    if d.is_integer():
      ans += 1
print(ans)
