N = int(input())
d = [int(x) for x in input().split()]

sum_ = 0
for i in range(N-1):
    for j in range(i+1, N):
        sum_ += d[i]*d[j]
print(sum_)
