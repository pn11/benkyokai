# WA
N, X = [int(a) for a in input().split()]

def burger(N):
    if N == 0:
        return "B"
    burg_pre = burger(N-1)
    return "B" + burg_pre + "P" + burg_pre + "P"

print(burger(N))