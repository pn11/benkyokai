import io
import re
import sys
_INPUT_ = """\
8691 20
"""
#sys.stdin = io.StringIO(_INPUT_)
N, K = [int(x) for x in input().split()]

for _ in range(K):
    # print(N)
    if N % 200 == 0:
        N //= 200
    else:
        N = int(str(N) + '200')

print(N)
