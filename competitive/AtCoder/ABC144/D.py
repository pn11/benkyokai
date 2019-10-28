import math

a, b, x = [int(x) for x in input().split()]

if x/a/a > b/2:
    print(180/3.141592*math.atan(2*(b - x/a/a)/a))
else:

    print(180/3.141592*math.atan(0.5*a*b*b/x))
