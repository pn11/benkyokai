import io
import re
import sys
from itertools import combinations
import numpy as np
from math import factorial
_INPUT_ = """\
6
2013 1012 2765 2021 508 6971
"""
sys.stdin = io.StringIO(_INPUT_)
N = int(input())
A = sorted([int(x) for x in input().split()])
A =  np.array(A)

A = A%200

cnt = min(N, 8)
bk = [[0]]*200


def output(a):
    print(f"{len(a)} {' '.join([str(x) for x in a])}")

for i in range(1, 1<<cnt):
    sig = 0
    s = []
    for j in range(cnt):
        if i & (1<<j):
            s.append(j+1)
            sig += A[j]
            sig %= 200
    if len(bk[sig]) != 0:
        print('Yes')
        output(bk[sig])
        output(s)
        exit()
    else:
        bk[sig] = s

print('No')
