import io
import re
import sys
from itertools import combinations
import numpy as np
_INPUT_ = """\
10
6 7 5 18 2
3 8 1 6 3
7 2 8 7 7
6 3 3 4 7
12 8 9 15 9
9 8 6 1 10
12 9 7 8 2
10 3 17 4 10
3 1 3 19 3
3 14 7 13 1
"""
#sys.stdin = io.StringIO(_INPUT_)
N = int(input())
A = np.zeros((N,1), dtype=np.uint)
B = np.zeros((N,1), dtype=np.uint)
C = np.zeros((N,1), dtype=np.uint)
D = np.zeros((N,1), dtype=np.uint)
E = np.zeros((N,1), dtype=np.uint)
for i in range(N):
    a, b, c, d, e = [int(x) for x in input().split()]
    A[i] = a
    B[i] = b
    C[i] = c
    D[i] = d
    E[i] = e

max_score = 0

for c in combinations(range(N), 3):
    i1, i2, i3 = c
    maxA = A[[i1, i2, i3]].max()
    maxB = B[[i1, i2, i3]].max()
    maxC = C[[i1, i2, i3]].max()
    maxD = D[[i1, i2, i3]].max()
    maxE = E[[i1, i2, i3]].max()
    score = min(maxA, maxB, maxC, maxD, maxE)
    max_score = max(score, max_score)

print(max_score)
