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
5 1 3
"""
_INPUT_2 = """\
1 4 3
"""
_INPUT_3 = """\
5 5 5
"""

def solve():
    A = [int(x) for x in input().split()]
    A = sorted(A)
    if A[2] - A[1] == A[1] - A[0]:
        print('Yes')
    else:
        print('No')
    

if __file__ != './Main.py':
    sys.stdin = io.StringIO(_INPUT_1)
    solve()
    sys.stdin = io.StringIO(_INPUT_2)
    solve()
    sys.stdin = io.StringIO(_INPUT_3)
    solve()
else:
    solve()
