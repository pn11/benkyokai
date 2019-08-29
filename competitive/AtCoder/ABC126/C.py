N, K = [int(a) for a in input().split()]

prob = 0

for i in range(1, N+1):
    j = i
    inverse_p = N
    while j < K:
        j *= 2
        inverse_p *= 2
    prob += 1/ inverse_p

print(prob)
