N, K, Q = [int(x) for x in input().split()]

seikai = [0] * N

for _ in range(Q):
    a = int(input())
    seikai[a-1] += 1

for i in range(N):
    if K - (Q - seikai[i]) > 0:
        print("Yes")
    else:
        print("No")
