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
3
Everest 8849
K2 8611
Kangchenjunga 8586
"""
_INPUT_2 = """\
4
Kita 3193
Aino 3189
Fuji 3776
Okuhotaka 3190
"""
_INPUT_3 = """\
4
QCFium 2846
chokudai 2992
kyoprofriends 2432
penguinman 2390
"""

def solve():
    N = int(input())
    M = []
    for _ in range(N):
        s, t =  [x for x in input().split()]
        M.append((s, int(t)))
    print(sorted(M, key=lambda x: -x[1])[1][0])

if __file__ != './Main.py':
    sys.stdin = io.StringIO(_INPUT_1)
    solve()
    sys.stdin = io.StringIO(_INPUT_2)
    solve()
    sys.stdin = io.StringIO(_INPUT_3)
    solve()
else:
    solve()
