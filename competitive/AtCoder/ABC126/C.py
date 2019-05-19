N, K = [int(a) for a in input().split()]

prob = 0

for i in range(1, N+1):
    j = i
    p = 1.0
    while j < K:
        j *= 2
        p *= 0.5
    prob += p

print(prob)
    
