N, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]


total = sum(a)
num = 0

if total == x:
    num = N
elif total < x:
    num = N -1
else:
    a.sort()
    cum = 0
    for i, aa in enumerate(a):
        cum += aa
        if cum > x:
            num = i
            break

print(num)
