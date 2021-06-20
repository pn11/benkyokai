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
12
"""
_INPUT_2 = """\
100128
"""
_INPUT_3 = """\
1 2 3
"""

def solve():
    N = int(input())
    SMALL = 1
    LARGE = 1000000000
    while True:
        i = (SMALL+LARGE) // 2
        v = ((1+i)*i)//2
        if v == N:
            day = i-
        elif v > N:
            LARGE = i
        elif v < N:



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
