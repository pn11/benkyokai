import io
import re
import sys
_INPUT_ = """\
5 896 483
228 59
529 310
339 60
78 266
659 391
"""
#sys.stdin = io.StringIO(_INPUT_)
N, D, H = [int(x) for x in input().split()]
print(D, H)
min_slope = 1000
ans = 0
for _ in range(N):
    d, h = [int(x) for x in input().split()]
    slope = (H - h) / (D - d)
    print(d, h, slope)
    if slope < min_slope:
        min_slope = slope
        ans = H - slope*D

print(max(ans, 0))