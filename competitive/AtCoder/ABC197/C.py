# 書きかけ
import numpy as np
N = int(input())
A = [int(x) for x in input().split()]

ans = 88888888

for i in range(2**N):
    print(bin(i))
    b = str(bin(i))[2:]
    b = b.zfill(N)
    print(b)
    ORs = []
    tmp_value = 0
    for j in range(N-1):
        tmp_value |= j
        if b[j] == '1':
            ORs.append(tmp_value)
            tmp_value = 0
    tmp_ans = ORs[0]

    for a in ORs[1:]:
        tmp_ans ^= a
    ans = min(ans, tmp_ans)
