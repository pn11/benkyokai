import io
import re
import sys

_INPUT_ = """\
hellospaceRhellospace
"""
#sys.stdin = io.StringIO(_INPUT_)

def solve(S):
    r_flag = False
    T = ""
    for i in range(len(S)):
        s = S[i]
        if s == 'R':
            r_flag = not r_flag
            continue
        if r_flag:
            if len(T) > 0 and T[0] == s:
                T = T[1:]
            else:
                T = s + T
        else:
            if len(T) > 0 and T[-1] == s:
                T = T[:-1]
            else:
                T += s
    if r_flag:
        return T[::-1]
    else:
        return T

S = input()
print(solve(S))
