line1 = input().split()
line2 = input()

n_short = int(line1[0])
n_cheese = int(line1[1])
n_customer = int(line1[2])


for i in range(n_customer):
    customer = line2[i]
    if customer == 'S':
        if n_short > 0:
            n_short -= 1
    elif customer == 'C':
        if n_cheese > 0:
            n_cheese -= 1
    elif customer == 'E':
        if n_short >= n_cheese:
            if n_short > 0:
                n_short -= 1
        else:
            if n_cheese > 0:
                n_cheese -= 1

print(n_short)
print(n_cheese)
