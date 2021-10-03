import bisect
from collections import deque
from copy import deepcopy
from fractions import Fraction
from functools import reduce
import heapq as hq
import io
from itertools import combinations, permutations
import math
from math import factorial
import re
import sys
sys.setrecursionlimit(10000)

#from numba import njit
import numpy as np

_INPUT_1 = """\
3 220
100 50 102
"""
_INPUT_2 = """\
5 2
1 1 1 1 1
"""

多分同じ数がある場合 WA になる


def solve():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    A = sorted(A, reverse=True)
    A.append(0)

    range1 = []
    for i, _ in enumerate(A):
        if i +1 >= N+1:
            break
        diff = A[i] - A[i+1]
        range1.append(diff*(i+1))
    range1 = np.cumsum(range1).tolist()

    a = bisect.bisect_left(range1, K)
    #print(N, K, range1, a)

    ans = 0
    #print(A)
    for aa in range(a):
        num_dup = aa+1
        ans += num_dup * (A[aa] + A[aa+1]+1)*(A[aa]-A[aa+1])/2
    #print(ans)

    dd = (K-range1[a-1])
    if a < N:
        num_dup = a+1
        dd2 = dd // num_dup
        res = dd % num_dup
        print(num_dup, dd, dd2, res)
        ans += num_dup * ((A[a]-dd2+1)+(A[a]))*dd2/2
        #print(ans)
        ans += res * A[a]-dd2

    print(int(ans))


if __file__ != './Main.py':
    if '_INPUT_1' in globals():
        sys.stdin = io.StringIO(_INPUT_1)
        solve()
    if '_INPUT_2' in globals():
        sys.stdin = io.StringIO(_INPUT_2)
        solve()
    if '_INPUT_3' in globals():
        sys.stdin = io.StringIO(_INPUT_3)
        solve()
else:
    solve()
