import math
import numpy as np

Nstr = input()
N = int(Nstr)
S_N = 0

for n in Nstr:
    S_N += int(n)

if N % S_N == 0:
    print("Yes")
else:
    print("No")

