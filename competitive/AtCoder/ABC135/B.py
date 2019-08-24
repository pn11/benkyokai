N = int(input())
p = [int(pp) for pp in input().split()]

error_pos = []

for i in range(N-1):
    if p[i] > p[i+1]:
        error_pos.append(i)
print(error_pos)

if len(error_pos) == 0:
    print("YES")
elif len(error_pos) == 1:
    tmp = p[error_pos[0]]
    p[error_pos[0]] = p[error_pos[1]]
    p[error_pos[1]] = tmp
elif len(error_pos) == 2:
	pass
else:
    print("NO")
