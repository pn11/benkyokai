N, K = [int(a) for a in input().split()]
S = input()
newS = ""

for i, _ in enumerate(S):
    if i == K-1:
        newS += S[i].lower()
    else:
        newS += S[i]

print(newS)
