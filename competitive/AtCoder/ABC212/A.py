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
50 50
"""
_INPUT_2 = """\
100 0
"""
_INPUT_3 = """\
0 100
"""

def solve():
    A, B = [int(x) for x in input().split()]
    if 0 < A and B == 0:
        print('Gold')
    elif A == 0 and 0 < B:
        print('Silver')
    else:
        print('Alloy')

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
