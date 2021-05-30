import io
import re
import sys
from itertools import combinations
import numpy as np
from math import factorial
_INPUT_ = """\
6
2013 1012 2765 2021 508 6971
"""
sys.stdin = io.StringIO(_INPUT_)
N = int(input())
A = sorted([int(x) for x in input().split()])
A =  np.array(A)

A = A%200

for i in range(200):

    
dp[0] = 0



cumA = np.cumsum(A)
#cumA %= 200

print(A)
print(cumA)
