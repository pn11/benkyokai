N = int(input())

ans = 'No'
for i in range(1, 10):
    if N % i == 0:
        res = N // i
        if res < 10:
            ans = 'Yes'

print(ans)

