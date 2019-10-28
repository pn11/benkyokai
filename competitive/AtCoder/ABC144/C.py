import math
N = int(input())

sqN = math.floor(math.sqrt(N))
yaku1 = 1
yaku2 = 1
for i in range(sqN, 0, -1):
    if N % i == 0:
        yaku1 = i
        yaku2 = N // i
        break

print(yaku1+yaku2-2)
    
