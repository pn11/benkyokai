N = int(input())
A = [int(x) for x in input().split()]
newA = [None]*N

for i, a in enumerate(A):
    newA[a-1] = str(i+1)

print(" ".join(newA))
