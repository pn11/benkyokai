import numpy as np
H, W, X, Y = [int(x) for x in input().split()]
X -= 1
Y -= 1

arr = np.zeros(shape=(H, W))
for y in range(H):
    s = input()
    for x in range(W):
        arr[y, x] = 1 if s[x] == '#' else 0

ans = 1 # 自分自身

a = arr[X, :]
cuma = np.cumsum(a) 
for y in range(W):
    if y == Y:
        continue
    if a[y] == 1:
        continue
    if cuma[y] == cuma[Y]:
        ans += 1

b = arr[:, Y]
cumb = np.cumsum(b) 
for x in range(H):
    if x == X:
        continue
    if b[x] == 1:
        continue
    if cumb[x] == cumb[X]:
        ans += 1

print(ans)
