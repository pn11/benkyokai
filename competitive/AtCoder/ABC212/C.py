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
2 2
1 6
4 9
"""
_INPUT_2 = """\
1 1
10
10
"""
_INPUT_3 = """\
6 8
82 76 82 82 71 70
17 39 67 2 45 35 22 24
"""

def solve():
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    A = sorted(A)
    B = sorted(B)

    min_min_abs = 1000000000
    for a in A:
        num = bisect.bisect_left(B, a, lo=0, hi=len(B))
        if num == 0:
            min_abs = abs(B[0] - a)
        elif num == len(B):
            min_abs = abs(B[num-1] - a)
        else:
            min_abs = min(abs(B[num-1]-a), abs(B[num]-a))
        
        min_min_abs = min(min_abs, min_min_abs)
    print(min_min_abs)


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
