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
ooo???xxxx
"""
_INPUT_2 = """\
o?oo?oxoxo
"""
_INPUT_3 = """\
xxxxx?xxxo
"""


def solve():
    S = input()
    ans = 0

    def check(num, i):
        for ss in num:
            if ss == i:
                return True
        else:
            return False

    for i in range(10000):
        num = str(i).zfill(4)
        ok = True
        for j, s in enumerate(S):
            if s == 'o':
                if check(num, str(j)):
                    pass
                else:
                    ok = False
                    break
            if s == 'x':
                if not check(num, str(j)):
                    pass
                else:
                    ok = False
                    break
        if ok:
            ans += 1

    print(ans)


if __file__ != './Main.py':
    sys.stdin = io.StringIO(_INPUT_1)
    solve()
    sys.stdin = io.StringIO(_INPUT_2)
    solve()
    sys.stdin = io.StringIO(_INPUT_3)
    solve()
else:
    solve()
