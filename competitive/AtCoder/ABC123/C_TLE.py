'''シミュレーションすると人数が多いときに間に合わない。'''
import numpy as np


num_man = [0] * 6
diff_rate = [0] * 5

N = int(input())
num_man[0] = N

for i in range(5):
    diff_rate[i] = int(input())


def move():
    num_move = [0]*5
    for i in range(5):
        if num_man[i] == 0:
            continue
        num_move[i] = min(diff_rate[i], num_man[i])

    for i in range(5):
        num_man[i] -= num_move[i]
        num_man[i+1] += num_move[i]
    
t = 0

while True:
    move()
    t += 1
    
    if num_man[5] == N:
        break




print(t)
