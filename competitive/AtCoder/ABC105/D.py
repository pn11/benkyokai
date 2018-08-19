# TLE

import numpy as np

line = input().split()
N = int(line[0])
M = int(line[1])
line = input().split()
A = [0]

A.extend([int(l) for l in line])

numA = np.array(A, np.int64)
cumA = np.cumsum(numA)
length = cumA.shape[0]

num = 0
for i in range(length):
    for j in range(i+1, length):
        if (cumA[j] - cumA[i]) % M == 0:
            num += 1
print(num)
