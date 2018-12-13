N = int(input())

max = 0
sum = 0

for i in range(N):
    p = int(input())
    sum += p
    
    if p > max:
        max = p

sum -= max // 2

print(sum)
