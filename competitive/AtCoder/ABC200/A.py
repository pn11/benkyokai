import io
import re
import sys
_INPUT_ = """\
2021
"""
#sys.stdin = io.StringIO(_INPUT_)
N = int(input())

ans = (N-1) // 100 +1
print(ans)
