N = int(input())
d = [int(a) for a in input().split()]

d = sorted(d)

lower = d[N//2 -1]
upper = d[N//2]

print(len(range(lower, upper)))
