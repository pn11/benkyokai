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
import statistics
import sys

#from numba import njit
from scipy import ndimage, misc
import numpy as np

_INPUT_1 = """\
3 2
1 7 0
5 8 11
10 4 2
"""
_INPUT_2 = """\
3 3
1 2 3
4 5 6
7 8 9
"""
_INPUT_3 = """\
1 2 3
"""

def solve():
    N, K = [int(x) for x in input().split()]
    A = []
    for _ in range(N):
        A.append([int(x) for x in input().split()])
    A = np.array(A)
    medians = []
    #print(A)
    for i in range(N-K+1):
        for j in range(N-K+1):
            #print(A[i:i+K, j:j+K])
            #print(A[i:i+K, j:j+K].flatten().tolist())
            medians.append(statistics.median_low(A[i:i+K, j:j+K].flatten().tolist()))
    #print(medians)
    print(min(medians))
    #median = ndimage.median_filter(A, size=K)
    #print(median)


if __file__ != './Main.py':
    sys.stdin = io.StringIO(_INPUT_1)
    solve()
    sys.stdin = io.StringIO(_INPUT_2)
    solve()
    #sys.stdin = io.StringIO(_INPUT_3)
    #solve()
else:
    solve()
