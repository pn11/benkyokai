import numpy as np
import math

line = input().split()
x1 = int(line[0])
y1 = int(line[1])
x2 = int(line[2])
y2 = int(line[3])

a = x2-x1
b = y2-y1
r = math.sqrt(a*a + b*b)


x3 = x2 - b
y3 = y2 + a
x4 = x3 - a
y4 = y3 - b

print("{} {} {} {}".format(x3, y3, x4, y4))
