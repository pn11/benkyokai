'''ABC 116 C
要は何回登り（下り）があるか数えるだけ。
'''
import numpy as np

N = int(input())
h = [int(a) for a in input().split()]
h = np.array([0] + h + [0]) # 最初と最後をゼロ埋め

diff = np.diff(h)

print(np.sum(diff[diff>0]))
