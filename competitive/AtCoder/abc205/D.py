import bisect
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
4 3
3 5 6 7
2
5
3
"""
_INPUT_2 = """\
5 2
1 2 3 4 5
1
10
"""


def solve():
    N, Q = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A = sorted(A)
    #print(A)

    for _ in range(Q):
        K = int(input())
        iniK = K
        num_prev = 0
        while True:
            #print(f"{num_prev=}, {K=}")
            num = bisect.bisect_right(A, K, lo=0, hi=len(A))
            K = iniK + num
            if num == len(A):
                break
            if num_prev == num:
                break
            num_prev = num
        
        print(iniK+num)



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
