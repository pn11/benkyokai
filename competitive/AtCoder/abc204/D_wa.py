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

#from numba import njit
import numpy as np

_INPUT_1 = """\
5
8 3 7 2 5
"""
_INPUT_2 = """\
2
1000 1
"""
_INPUT_3 = """\
9
3 14 15 9 26 5 35 89 79
"""

def solve():
    N = int(input())
    T = sorted([int(x) for x in input().split()], reverse=True)

    sum1 = 0
    sum2 = 0
    sum1 = 0
    ans = 100000
    
    for c in combinations(range(N), 2):
        i1, i2 = c
    ans = min(ans, max())
            sum1 += 1
    print(sum1)

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
