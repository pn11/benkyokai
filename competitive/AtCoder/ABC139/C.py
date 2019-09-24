N = int(input())
H = [int(a) for a in input().split()]

streak = 0
prev = 0
ans = 0

for h in H:
    if prev >= h:
        streak += 1
        ans = max(ans, streak)
    else:
        streak = 0
    prev = h

print(ans)
