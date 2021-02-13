V, T, S, D = [int(x) for x in input().split()]

t1 = D/V

if T <= t1 and t1 <= S:
    print("No")
else:
    print("Yes")
