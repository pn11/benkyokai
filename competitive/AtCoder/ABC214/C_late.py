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
#import numpy as np

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
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    for i in range(N*2):
        T[(i+1)%N] = min(T[(i+1)%N], T[i%N] + S[i%N])
    for ans in T:
        print(ans)


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
