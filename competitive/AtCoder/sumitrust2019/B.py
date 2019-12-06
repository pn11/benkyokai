import math
N = int(input())

ans = None
for i in range(1, 50001):
    v = math.floor(i * 1.08)
    if v == N:
        ans = i
if ans is not None:
    print(ans)
else:
    print(":(")
