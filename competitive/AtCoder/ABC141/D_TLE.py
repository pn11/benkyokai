N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

for _ in range(M):
    A = sorted(A, reverse=True)
    if A[0] == 0:
        break
    A[0] //= 2

print(sum(A)) 