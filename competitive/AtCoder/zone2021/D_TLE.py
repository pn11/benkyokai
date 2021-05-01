import io
import re
import sys
from numba import njit
_INPUT_ = """\
hellospaceRhellospace
"""
#sys.stdin = io.StringIO(_INPUT_)

@njit
def solve(S):
    T = ""
    for i in range(len(S)):
        s = S[i]
        if s == 'R':
            T = T[::-1]
        else:
            if len(T) > 0 and T[-1] == s:
                T = T[:-1]
            else:
                T += s
    return T

S = input()
print(solve(S))
