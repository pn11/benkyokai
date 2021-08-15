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
3
4 1 5
3 10 100
"""
_INPUT_2 = """\
4
100 100 100 100
1 1 1 1
"""
_INPUT_3 = """\
4
1 2 3 4
1 2 4 7
"""

def solve():
    N = int(input())
    S = [int(x) for x in input().split()]
    T = [int(x) for x in input().split()]
    min_time = T[:]
    maxT = max(T)
    #distance[]

    cumsum = np.cumsum(S+S, axis=0).tolist()
    #print(cumsum)

    for i in range(N-1, -1, -1):
        for j in range(i-1, i-N,-1):
            if j < 1:
                diff_time = cumsum[N+i-1] - cumsum[N+j-1]
            else:
                diff_time = cumsum[i-1] - cumsum[j-1]
            #print(i, j, diff_time, T[i], T[j]+diff_time)
            min_time[i] = min(min_time[i], T[j]+diff_time)

    for i in range(N):
        print(min_time[i])


if __file__ != './Main.py':
    if '_INPUT_1' in globals():
        sys.stdin = io.StringIO(_INPUT_1)
        solve()
        print('====')
    if '_INPUT_2' in globals():
        sys.stdin = io.StringIO(_INPUT_2)
        solve()
        print('====')
    if '_INPUT_3' in globals():
        sys.stdin = io.StringIO(_INPUT_3)
        solve()
        print('====')
else:
    solve()
