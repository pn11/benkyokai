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
#import numpy as np

_INPUT_1 = """\
5
1 3
1 5
3
2 2
3
"""
_INPUT_2 = """\
6
1 1000000000
2 1000000000
2 1000000000
2 1000000000
2 1000000000
3
"""


def solve():
    Q = int(input())

    bag = []
    added_value = 0
    for _ in range(Q):
        line = input()
        if line[0] == '1':
            x = int(line.split()[1])
            hq.heappush(bag, (x-added_value, x-added_value)) 
        elif line[0] == '2':
            x = int(line.split()[1])
            added_value += x
        elif line[0] == '3':
            priority, x = hq.heappop(bag)
            print(x+added_value)


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
