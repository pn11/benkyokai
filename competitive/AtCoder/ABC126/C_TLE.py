from fractions import Fraction

N, K = [int(a) for a in input().split()]

prob = 0

for i in range(1, N+1):
    j = i
    num_omote = 0
    while j < K:
        j *= 2
        num_omote += 1
    prob += Fraction(1, N) * Fraction(1, 2)**num_omote

print(float(prob))
    
