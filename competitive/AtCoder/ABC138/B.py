N = int(input())
A = [int(a) for a in input().split()]

sum = 0
for a in A:
    sum += 1/a
print(1/sum)
