import numpy as np
N, M = [int(a) for a in input().split()]

A = []
B = []

#dp = np.zeros((10000, 100000), dtype=np.int64)
#dp = {}

for _ in range(N):
    a, b = input().split()
    A.append(int(a))
    B.append(int(b))


def choose(A, B, used_ind, remained_days, sum):
    print(used_ind, remained_days, sum)
    max_B = 0
    max_ind = -1
    for i in range(N):
        if i in used_ind:
            continue
        if A[i] > remained_days:
            continue
        if B[i] > max_B:
            max_ind = i
            max_B = B[i]
    remained_days -= A[max_ind]
    sum += max_B
    used_ind.append(max_ind)
    return max_ind

used_ind = []
remained_days = M
sum = 0

while choose(A, B, used_ind, remained_days, sum) != -1:
    print("Not Yet")

print(sum)