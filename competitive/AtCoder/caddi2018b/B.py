N, H, W = [int(i) for i in input().split()]

count = 0

for _ in range(N):
    A, B = [int(i) for i in input().split()]
    if A >= H and B >= W:
        count += 1

print(count)
