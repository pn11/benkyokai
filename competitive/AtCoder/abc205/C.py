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
3 2 4
"""
_INPUT_2 = """\
-7 7 2
"""
_INPUT_3 = """\
-8 6 3
"""

def check(a, b):
    if a == b:
        print('=')
    elif a > b:
        print('>')
    else:
        print('<')


def solve():
    A, B, C = [int(x) for x in input().split()]
    if C % 2 == 0:
        check(abs(A), abs(B))
    else:
        check(A, B)



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
