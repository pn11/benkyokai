N = int(input())
B = [int(a) for a in input().split()]
B = [B[0]] + B + [B[-1]]

ans = 0
for i in range(N):
    a = min(B[i], B[i+1])
    ans += a
print(ans)
