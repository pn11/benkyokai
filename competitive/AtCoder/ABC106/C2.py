import math

S = input()
K = int(input())

n1 = 0
first_non1 = 0
for s in S:
    sint = int(s)
    if sint == 1:
        n1 += 1
    else:
        first_non1 = sint
        break


if K <= n1:
    print(1)
else:
    print(first_non1)
