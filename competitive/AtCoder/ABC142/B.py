import numpy as np
N, K = [int(x) for x in input().split()]
h = np.array([int(x) for x in input().split()])
print(len(h[h>=K]))
