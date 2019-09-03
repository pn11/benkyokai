A, B, T = [int(x) for x in input().split()]

ans = B
while True:
  ans += (B-A)
  if ans >= T:
    print(ans)
    break
