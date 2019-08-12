A, B = [int(a) for a in input().split()]
print(max(max(A+B, A-B), A*B))
