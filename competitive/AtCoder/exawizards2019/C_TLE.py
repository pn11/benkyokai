"""普通に書いたやつ。TLE"""
import numpy as np
import math

N, Q = [int(a) for a in input().split()]
symbol = input()

target = [None]*Q
direction = [None]*Q

num_golems = [1]*N
num_golems_next = [1]*N

for i in range(Q):
    line = input().split()
    target[i] = line[0]
    direction[i] = line[1]    

for i in range(Q):
    for j in range(N):
        num_golems[j] = num_golems_next[j]
    for j in range(N):
        if symbol[j] == target[i]:
            num_golems_next[j] -= num_golems[j]

            if direction[i] == 'L':
                next_index = j - 1
            elif direction[i] == 'R':
                next_index = j + 1

            
            if next_index == -1 or next_index == N:
                continue
            
            num_golems_next[next_index] += num_golems[j]

    # print(target[i], direction[i], num_golems, '->', num_golems_next)

sum = 0
for j in range(N):
    sum += num_golems_next[j]

print(sum)

