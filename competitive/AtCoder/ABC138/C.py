N = int(input())
v = [int(a) for a in input().split()]

v = sorted(v)

def rec(i):
    if i == 0:
        return v[0]
    return (v[i] + rec(i-1))*0.5

print(rec(N-1))
