'''ボトルネックのとこだけ考えれば良い。'''
import numpy as np
import math

diff_rate = [0] * 5

N = int(input())

for i in range(5):
    diff_rate[i] = int(input())

min_rate = np.min(diff_rate)



print(math.ceil(N/min_rate) + 4)
