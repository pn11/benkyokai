import math
import numpy as np

#line = input().split()
#N = int(line[0])
N = int(input())
line = input().split()
A = [int(a) for a in line]


min_ = 1e9
max_ = 1

for a in A:
    max_ = max(max_, a)
    min_ = min(min_, a)

print(max_-min_)
