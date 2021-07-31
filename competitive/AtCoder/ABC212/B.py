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
7777
"""
_INPUT_2 = """\
0112
"""
_INPUT_3 = """\
9012
"""

def solve():
    X = [int(s) for s in input()]
    if X[0] == X[1] and X[0] == X[2] and X[0] == X[3]:
        print('Weak')
        return
    def is_next(a, b):
        if a == 9 and b == 0:
            return True
        if a + 1 == b:
            return True
        return False
    if is_next(X[0], X[1]) and is_next(X[1], X[2]) and is_next(X[2], X[3]):
            print('Weak')
            return
    print('Strong')


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
