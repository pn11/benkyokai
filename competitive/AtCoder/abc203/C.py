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
2 3
2 1
5 10
"""
_INPUT_2 = """\
5 1000000000
1 1000000000
2 1000000000
3 1000000000
4 1000000000
5 1000000000
"""
_INPUT_3 = """\
3 2
5 5
2 1
2 2
"""

def solve():
    N, K = [int(x) for x in input().split()]
    A = []
    for _ in range(N):
        a, b = [int(x) for x in input().split()]
        A.append((a, b))
    A = sorted(A, key=lambda x: x[0])

    money = K
    current = 0

    for i in range(N):
        #print("money = ",money, "current = ", current)
        if money + current >= A[i][0]:
            money -= (A[i][0]-current)
            money += A[i][1]
            current = A[i][0]
            continue
        if current == A[i][0]:
            money += A[i][1]
            continue
        
    current = money + current

    print(current)

if __file__ != './Main.py':
    sys.stdin = io.StringIO(_INPUT_1)
    solve()
    sys.stdin = io.StringIO(_INPUT_2)
    solve()
    sys.stdin = io.StringIO(_INPUT_3)
    solve()
else:
    solve()
