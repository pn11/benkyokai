import bisect
A, B, X = [int(x) for x in input().split()]

def needed(N):
    return A*N+B*len(str(N))


def next(ileft, iright, X):
    center = (ileft+iright) // 2
    nd = needed(center)
 #   print(nd, X)
    if nd < X:
        nxleft, nxright = center, iright
    elif nd >= X:
        nxleft, nxright = ileft, center
    return nxleft, nxright

iright = 1000000000-1
ileft = 0

while True:
    ileft, iright = next(ileft, iright, X)
#    print(ileft, iright)
    if abs(ileft-iright) <= 1:
        break
ans = 0
for i in range(max(ileft-10, 0), min(ileft+10, 1000000001)):
#    print(i, needed(i), X)
    if needed(i) > X:
        break
    ans = i
print(ans)
