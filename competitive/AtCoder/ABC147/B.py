S = input()

l = len(S)

nhug = 0
for i in range(l//2):
    if S[i] != S[l-1-i]:
        nhug += 1

print(nhug)

