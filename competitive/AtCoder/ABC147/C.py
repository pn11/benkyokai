N = int(input())
x = []
y = []
# offsets
x.append([])
y.append([])
for i in range(N):
    A = int(input())
    xtmp = []
    ytmp = []
    for _ in range(A):
        xx, yy = [int(x) for x in input().split()]
        xtmp.append(xx)
        ytmp.append(yy)
    x.append(xtmp)
    y.append(ytmp)

num_honest = 0

for i in range(2**N):
    is_honest_inv = '{:015b}'.format(i) + '0' # add dummy
    is_honest = [int(is_honest_inv[15-i]) for i in range(N+1)]
    print(is_honest_inv, is_honest)
    is_ok = True
    for j in range(1, N+1):
        for xx, yy in zip(x[j], y[j]):
            print(xx, yy, is_honest[xx])
            if is_honest[j] == 1:
                if is_honest[xx] != yy:
                    is_ok = False
                    break
        if not is_ok:
            break
    if is_ok:
        num_honest = max(num_honest, sum(is_honest))
        print(f'OK: {num_honest}')
print(num_honest)
        
    
    
