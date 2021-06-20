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
3
1 7 1
"""
_INPUT_2 = """\
10
1 10 100 1000 10000 100000 1000000 10000000 100000000 1000000000
"""
_INPUT_3 = """\
20
7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4
"""

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    dicA = {}
    for a in A:
        dicA[a] = dicA.get(a, 0) + 1

    #print(dicA)

    combi = N*(N-1) // 2
    chouhuku = 0
    for k, v in dicA.items():
        chouhuku += v*(v-1)//2

    print(combi - chouhuku)

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
