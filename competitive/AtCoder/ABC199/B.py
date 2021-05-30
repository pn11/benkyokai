import io
import math
import numpy as np
import re
import sys

_INPUT_1 = """\
2
3 2
7 5
"""

_INPUT_2 = """\
3
1 5 3
10 7 3
"""

_INPUT_3 = """\
3
3 2 5
6 9 8
"""

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    ANS = min(B) - max(A) + 1

    if ANS < 1:
        print(0)
    else:
        print(ANS)


if __file__ != './Main.py':
    sys.stdin = io.StringIO(_INPUT_1)
    solve()
    sys.stdin = io.StringIO(_INPUT_2)
    solve()
    sys.stdin = io.StringIO(_INPUT_3)
    solve()
else:
    solve()
