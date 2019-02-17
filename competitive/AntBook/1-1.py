
def solve(n, m, k):
    ncard = len(k)

    for i1 in range(ncard):
        n1 = k[i1]
        for i2 in range(ncard):
            n2  = k[i2]
            for i3 in range(ncard):
                n3 = k[i3]
                for i4 in range(ncard):
                    if n1 + n2 + n3 + k[i4] == m:
                        print("Yes")
                        return

    print("No")
    return




n: int = 3
m: int = 10
k = (1, 3, 5)
solve(n, m, k)

solve(3, 9, (1, 3, 5))