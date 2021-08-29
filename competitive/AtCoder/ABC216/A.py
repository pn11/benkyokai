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
import numpy as np

_INPUT_1 = """\
15.8
"""
_INPUT_2 = """\
1.0
"""
_INPUT_3 = """\
12.5
"""

def solve():
    X, Y = [int(x) for x in input().split('.')]
    if 0 <= Y and Y <= 2:
        print(f"{X}-")
    elif Y <= 6:
        print(f"{X}")
    else:
        print(f"{X}+")
        

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
