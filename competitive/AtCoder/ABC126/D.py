'''読み込みだけ'''
import numpy as np

N = int(input())

array = np.zeros((N-1, 3), np.int64)
color = np.zeros((N-1, 1), np.int)

for i in range(N-1):
    array[i, :] = [int(a) for a in input().split()]


print(array)

