import bisect
from queue import Queue
from copy import deepcopy
from collections import deque

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
3 3
---
+-+
+--
"""
_INPUT_2 = """\
2 4
+++-
-+-+
"""
_INPUT_3 = """\
1 1
-
"""



def solve():
    H, W = [int(x) for x in input().split()]
    A = []
    for _ in range(H):
        A.append([1 if x == '+' else -1 for x in input()])
    A = np.array(A)
    print(A)

    d = []


    def bfs():
        que = Queue()
        for i in range(H):
            # turn taka ao
            d.append([(-1, 0, 0) for j in range(W)])
        print(d)

        que.put((0, 0))
        d[0][0] = (0, A[0,0], 0)

        turn = 0
        taka = 0
        ao = 0
        while not que.empty():
            i, j = que.get()

            if turn % 2 == 0:
                taka += A[i, j]
            else:
                ao += A[i,j]
            turn += 1
            d[i][j] = (turn, taka, ao)
            
            if i == H-1 and j == W-1:
                break

            
            if i+1 < H-1 and d[i+1][j][0] == -1:
                que.put(i+1, j)
                d[i+1][j] = (turn, -1, -1 )
            
        
    bfs()

'''
        if turn % 2 == 0:
            taka += A[i, j]
        else:
            ao += A[i,j]
        turn += 1

        if i == H-1 and j == W-1:
            return turn, taka, ao
        else:
            if i < H-1:
                dfs(i+1, j, turn, taka, ao)
            elif j <
            dfs(i, j+1)
'''
    
    

if __file__ != './Main.py':
    sys.stdin = io.StringIO(_INPUT_1)
    solve()
    sys.stdin = io.StringIO(_INPUT_2)
    solve()
    sys.stdin = io.StringIO(_INPUT_3)
    solve()
else:
    solve()
