import bisect
from fractions import Fraction
from functools import reduce
import heapq as hq
import io
from itertools import combinations, permutations
import math
from math import factorial
import sys

#from numba import njit
import numpy as np

_INPUT_ = """\
10 10 10
"""
if __file__ != './Main.py':
    sys.stdin = io.StringIO(_INPUT_)

A, B, C = [int(x) for x in input().split()]

if A*A + B*B < C*C:
    print('Yes')
else:
    print('No')
