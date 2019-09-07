A, B = [int(a) for a in input().split()]

outlet = 1
ans = 0

while outlet < B:
    outlet += A-1
    ans += 1

print(ans)
