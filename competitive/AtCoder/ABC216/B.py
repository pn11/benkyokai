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
3
tanaka taro
sato hanako
tanaka taro
"""
_INPUT_2 = """\
3
saito ichiro
saito jiro
saito saburo
"""
_INPUT_3 = """\
4
sypdgidop bkseq
sypdgidopb kseq
ozjekw mcybmtt
qfeysvw dbo
"""

def solve():
    N = int(input())
    D = {}
    for _ in range(N):
        s, t = [x for x in input().split()]
        S = D.get(s, set())
        S.add(t)
        D[s] = S

    num = 0
    for k, v in D.items():
        num += len(v)
    
    if num != N:
        print('Yes')
    else:
        print('No')


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
