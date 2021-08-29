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
2 2
2
1 2
2
1 2
"""
_INPUT_2 = """\
2 2
2
1 2
2
2 1
"""


def solve():
    N, M = [int(x) for x in input().split()]
    num = []

    for _ in range(M):
        k = int(input())
        num.append([int(x) for x in input().split()])
    
    
    print(num)

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
