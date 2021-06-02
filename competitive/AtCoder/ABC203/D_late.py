# 二分探索 + 二次元累積和 (いもす法)
# 1. 二分探索でNxNの二次元配列の各要素がある値mより上か下か判定して、KxKの配列の和を計算
# 2. 二次元累積和を使って KxK の和の計算を高速化。KxK配列の和がK*Kとなる最小のmが答え。
# Thanks to https://atcoder.jp/contests/abc203/submissions/23133998
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
from numpy.core.numeric import convolve

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


def solve():
    N, K = [int(x) for x in input().split()]
    A = []
    for _ in range(N):
        A.append([int(x) for x in input().split()])
    A = np.array(A)
    # print(A)

    def cumsum2d(arr):
        s = arr.shape
        a = np.zeros(shape=(s[0]+1, s[1]+1), dtype=np.int64)
        a[1:, 1:] = np.cumsum(np.cumsum(arr, axis=0), axis=1)
        return a

    #cumsum2d(A)

    UP = 1000000000
    LOW = -1
    L = K*K//2+1

    def check(cummedA):
        for i in range(N-K+1):
            for j in range(N-K+1):
                sumK = cummedA[i+K, j+K] - cummedA[i, j+K] - cummedA[i+K, j] + cummedA[i,j]
                # print(f"{i=}, {j=}")
                # print(f"{cummedA[i+K, j+K]=}, {cummedA[i, j+K]=}, {cummedA[i+K, j]=}, {cummedA[i,j]=}")
                if sumK < L:
                    return True
        return False

    def check_para(cummedA):
        A1 = cummedA[:]
        A2 = np.zeros_like(cummedA)
        # y方向にKずらす
        A2[K:,:] = cummedA[:-K,:]
        A3 = np.zeros_like(cummedA)
        # x方向にKずらす
        A3[:,K:] = cummedA[:,:-K]
        A4 = np.zeros_like(cummedA)
        # xy方向にKずらす
        A4[K:,K:] = cummedA[:-K,:-K]
        #print(f"{A1=}, {A2=}, {A3=}, {A4=}")
        sumA = A1 + A4 - A2 - A3
        if np.any(sumA[K:,K:]<L):
            return True
        else:
            return False

    while UP > LOW+1:
        #print(UP, LOW)
        med = (UP + LOW) // 2
        # print(f"{med=}")
        medA = (A > med).astype(np.int64)
        # print(f"{medA=}")
        cummedA = cumsum2d(medA)
        # print(f"{cummedA=}")
        #if check(cummedA):
        if check_para(cummedA):
            UP = med
        else:
            LOW = med
        # print(LOW, UP)
    # print(f"{LOW=} {UP=}")
    print(UP)


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
