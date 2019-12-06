import bisect
import numpy as np
N = int(input())
S = input()

dic_ = {}
array =  np.zeros((10, 300001), np.int8)

for i in range(N):
    array[int(S[i]), i] = 1

def get_first_pos(i, k):
    ar = array[i, k+1:]
    wh = np.where(ar>0)
    if len(wh[0]) > 0:
        return wh[0][0] + k+1
    return None

ans = 0

for i in range(10):
    x1 = get_first_pos(i, -1)
    if x1 is None:
        continue
    for j in range(10):
        x2 = get_first_pos(j, x1)
        if x2 is None:
            continue
        for k in range(10):
            x3 = get_first_pos(k, x2)
            if x3 is None:
                continue
            ans += 1

print(ans)
