'''独立したグループがいくつかあるか数えれば良い。未完。'''

groups = []

N, M = [int(a) for a in input().split()]

for _ in range(M):
    x, y, _ = [int(a) for a in input().split()]
    groups.append({x, y})
