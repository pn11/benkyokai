import bisect
N = int(input())
L = [int(x) for x in input().split()]
L = sorted(L)
num_triangle = 0

for i in range(N-1, 1, -1):
    a = L[i]
    for j in range(i-1, 0, -1):
        b = L[j]
        c = L[j-1]
        if not a < b+c:
            break
#        print(a, b, L[:j], a-b, bisect.bisect_right(L[:j], a-b))
        num_triangle += len(L[:j]) - bisect.bisect_right(L[:j], a-b)

print(num_triangle)
