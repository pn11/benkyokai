# WA
import math

S = input()
K = float(input())
klog = math.log(K)

poslog = 0
for s in S:
    poslog += 5e11*math.log(float(s))
    if klog <= poslog:
        print(s)
        break
