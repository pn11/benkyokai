N, M = [int(x) for x in input().split()]
AB = []
for _ in range(N):
    AB.append([int(x) for x in input().split()])

AB = sorted(AB, key=lambda x: x[0])

current_drinks = 0
current_buget = 0
for a, b in AB:
    num_buy = min(b, (M-current_drinks))
    current_drinks += num_buy
    current_buget += num_buy*a
    # print(current_drinks, current_buget)
    if current_drinks == M:
        break
print(current_buget)
