import math
import numpy as np
line = input()

num = 0
for a in line:
    if a == '+':
        num += 1
    else:
        num -= 1

print(num)
