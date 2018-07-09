import math
import numpy as np


def count_2(n):
    i = 0
    while True:
        if n % 2 == 0:
            i += 1
            n = n // 2
        else:
            break
    return i

N = int(input())

a = [int(b) for b in input().split()]

sum = 0
for aa in a:
    sum += count_2(aa)

print(sum)
