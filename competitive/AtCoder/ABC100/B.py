import math
import numpy as np
 
line = input().split()
D = int(line[0])
N = int(line[1])
 
if D == 0:
    if N == 100:
        print(N+1)
    else:
        print(N)
elif D == 1:
    if N == 100:
        print((N+1)*100)
    else:
        print(N*100)
else :
    if N == 100:
        print((N+1)*10000)
    else:
        print(N*10000)
        
