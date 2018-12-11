N, T = [int(a) for a in input().split()]

minc = 9999

for i in range(N):
    c, t = [int(a) for a in input().split()]
    if t <= T:
        minc = min(c, minc)

if minc == 9999:
    print("TLE")
else:
    print(minc)
