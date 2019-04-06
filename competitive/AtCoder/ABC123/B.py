import numpy as np


def min_10(num):
    if num % 10 == 0:
        return num
    else:
        return ( num // 10 + 1 ) * 10

t = []

for _ in range(5):
    t.append(int(input()))

min_rem = 9
min_ind = 0

for i in range(len(t)):
    rem = t[i] % 10
    if rem == 0:
        continue
    if rem < min_rem:
        min_rem = rem
        min_ind = i

sum = 0

for i in range(len(t)):
    if i == min_ind:
        continue

    sum = min_10(sum) + t[i]


sum = min_10(sum) + t[min_ind]

print(sum)
