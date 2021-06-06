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
0 1
"""
_INPUT_2 = """\
0 0
"""

def solve():
    x, y = [int(x) for x in input().split()]
    if x == 0:
        if y == 0:
            print('0')
            return
        elif y == 1:
            print('2')
            return
        else:
            print('1')
            return
    elif x == 1:
        if y == 0:
            print('2')
            return
        elif y == 1:
            print('1')
            return
        else:
            print('0')
            return
    else:
        if y == 0:
            print('1')
            return
        elif y == 1:
            print('0')
            return
        else:
            print('2')
            return

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
