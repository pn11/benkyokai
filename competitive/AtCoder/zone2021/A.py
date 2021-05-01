import io
import re
import sys
_INPUT_ = """\
abcd
"""
#sys.stdin = io.StringIO(_INPUT_)
S = input()
m = re.findall('ZONe', S)
print(len(m))
