K, X = [int(a) for a in input().split()]

print(" ".join([str(i) for i in range(max(X-K+1, -10000), min(X+K-1, 10000)+1)]))
