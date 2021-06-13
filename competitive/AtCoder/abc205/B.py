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
5
3 1 2 4 5
"""
_INPUT_2 = """\
6
3 1 4 1 5 2
"""

_INPUT_3 = """\
3
1 2 3
"""

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    for i in range(1, N+1):
        if not i in A:
            print('No')
            return False
    print('Yes')
    return True

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
