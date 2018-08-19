N = int(input())

count = 0

for i in range(1, N+1, 2):
    yakusuu = 0
    for j in range(1, i+1, 2):
        if i % j == 0:
            yakusuu += 1
    if yakusuu == 8:
        count += 1

print(count)