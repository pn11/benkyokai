'''こういうのは苦手なので解説読んだ。解説は分かりやすいけど、次自力でやれと言われてもできる気がしない。'''
N = int(input())
A = [int(x) for x in input().split()]

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

L = [None]*(N+1)
R = [None]*(N+1)
L[0] = 0
R[N] = 0

for i, _ in enumerate(A):
  L[i+1] = gcd(L[i], A[i])
  R[N-1-i] = gcd(R[N-i], A[N-1-i])

M = [gcd(L[i], R[i+1]) for i in range(N)]

print(max(M))
