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
2 5 2
"""
_INPUT_2 = """\
4 5 6
"""
_INPUT_3 = """\
1 1 1
"""

def solve():
    A, B, C = [int(x) for x in input().split()]
    if A == B and B == C:
        print(A)
    elif A == B:
        print(C)
    elif B == C:
        print(A)
    elif C == A:
        print(B)
    else:
        print(0)

if __file__ != './Main.py':
    sys.stdin = io.StringIO(_INPUT_1)
    solve()
    sys.stdin = io.StringIO(_INPUT_2)
    solve()
    sys.stdin = io.StringIO(_INPUT_3)
    solve()
else:
    solve()
