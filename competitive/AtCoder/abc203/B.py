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
1 2
"""
_INPUT_2 = """\
3 3
"""
_INPUT_3 = """\
1 2 3
"""

def solve():
    N, K = [int(x) for x in input().split()]
    sum = 0
    for n in range(1, N+1):
        for k in range(1, K+1):
            sum += int(f"{n}0{k}")
    print(sum)

if __file__ != './Main.py':
    sys.stdin = io.StringIO(_INPUT_1)
    solve()
    sys.stdin = io.StringIO(_INPUT_2)
    solve()
    #sys.stdin = io.StringIO(_INPUT_3)
    #solve()
else:
    solve()
