"""場所ごとのゴーレムの数を見るのではなく、ゴーレムがどこにいるかに注目。
外に出たゴーレムはスキップされるので C_TLE.py よりは速いかと思ったが、同じくらい。
NumPy使えばもう少しは速くなるはず。
"""
import numpy as np
import math

N, Q = [int(a) for a in input().split()]
symbol = input()

target = [None]*Q
direction = [None]*Q

current_position = [i for i in range(N)]

for i in range(Q):
    line = input().split()
    target[i] = line[0]
    direction[i] = line[1]    

for i in range(Q):
    for j in range(N):
        if current_position[j] == -1 or current_position[j] == N:
            continue
        
        if symbol[current_position[j]] == target[i]:
            if direction[i] == 'L':
                current_position[j] -= 1
            elif direction[i] == 'R':
                current_position[j] += 1

#    print(target[i], direction[i], current_position)

sum = 0
for j in range(N):
    if current_position[j] == -1 or current_position[j] == N:
        continue
    sum += 1

print(sum)
