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
3 3
1 2
2 3
3 2
"""
_INPUT_2 = """\
3 0
"""
_INPUT_3 = """\
4 4
1 2
2 3
3 4
4 1
"""

def solve():
    N, M = [int(x) for x in input().split()]
    G = [[] for i in range(0, N+1)]
    for _ in range(M):
        a, b = [int(x) for x in input().split()]
        G[a].append(b)

    def dfs(i):
        if visited[i]:
            return
        visited[i] = True
        for j in G[i]:
            dfs(j)

    ans = 0
    for i in range(1, N+1):
        visited = [False] * (N+1)
        dfs(i)
        ans += sum(visited)
    print(ans)


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
