N = int(input())
A = [0] + [int(a) for a in input().split()]
B = [0] + [int(a) for a in input().split()]
C = [0] + [int(a) for a in input().split()]

previous = -1
satisfaction = 0

for a in A[1:]:
    satisfaction += B[a]
    if previous == a-1:
        satisfaction += C[a-1]
    previous = a

print(satisfaction)
