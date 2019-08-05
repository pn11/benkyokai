N = int(input())
H = [int(a) for a in input().split()]

result = 'Yes'

if H[0] >= 1:
    H[0] -= 1

for i in range(N-1):
    diff = H[i+1] - H[i]
    if diff >= 1:
        H[i+1] -= 1
    elif diff == 0:
        pass
    elif diff < 0:
        result = 'No'
        break

print(result)
