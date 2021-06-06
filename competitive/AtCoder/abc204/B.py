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
3
6 17 28
"""
_INPUT_2 = """\
4
8 9 10 11
"""

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    S = 0
    for a in A:
        if a <11:
            continue
        else:
            S += a - 10
    print(S)

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
