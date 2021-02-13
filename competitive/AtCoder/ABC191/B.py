N, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A1 = []

for a in A:
    if a != X:
        A1.append(str(a))
print(" ".join(A1))
