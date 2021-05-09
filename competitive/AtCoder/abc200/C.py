import io
import re
import sys
from itertools import combinations
import numpy as np
from math import factorial
_INPUT_ = """\
8
199 100 200 400 300 500 600 200
"""
#sys.stdin = io.StringIO(_INPUT_)
N = int(input())
AA = [0 for _ in range(200)]
#print(AA)

for x in input().split():
    AA[int(x) % 200] += 1
#A = np.array([int(x) for x in input().split()]) % 200
#print(AA)

ans = 0
for c in AA:
    ans += c*(c-1) // 2

#print(u, counts)

print(ans)
