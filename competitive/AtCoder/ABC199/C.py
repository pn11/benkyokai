import math
R, X, Y = [int(x) for x in input().split()]

dist = math.sqrt(X*X+Y*Y)

if dist < R:
    print(2)
else:
    print(math.ceil(dist/R))
