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
8
1 5 3 2 5 2 3 1
"""
_INPUT_2 = """\
7
1 2 3 4 1 2 3
"""
_INPUT_3 = """\
1
200000
"""

def check(a):
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            return False
    return True



def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    setA = list(set(A))

    visited = []
    Q = deque()
    for i in range(len(setA)):
        visited.append([False for j in range(len(setA))])
        for j in range(len(setA)):
            Q.append((i, j))

    for p in permutations([i for i in range(len(setA))], 2):
        i, j = p
        x = setA[i]
        y = setA[j]
        print(x, y)
        visited[i][j] = True

    print(visited)
    print(check(A))

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
