'''TLE'''
import numpy as np
N, M = [int(a) for a in input().split()]

AB = []

for _ in range(N):
    a, b = input().split()
    AB.append((int(a), int(b)))

AB = sorted(AB, key=lambda x: x[0])

used_ind = []
sum = 0

for remained_days in range(M+1):
    max_B = 0
    max_ind = -1

    for i in range(N):
        if i in used_ind:
            continue
        if AB[i][0] > remained_days:
            break
        if AB[i][1] > max_B:
            max_ind = i
            max_B = AB[i][1]
    remained_days -= AB[max_ind][0]
    sum += max_B
    used_ind.append(max_ind)

print(sum)