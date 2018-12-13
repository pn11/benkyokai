N, K = [int(a) for a in input().split()]

h = []

for _ in range(N):
    h.append(int(input()))

sortedh = sorted(h)

min_ = 1e9

for i in range(N-K+1):
    diff = sortedh[i+K-1] - sortedh[i]
    min_ = min(min_, diff)

print(min_)
