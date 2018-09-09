import numpy as np

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
line = input().split()
N = int(line[0])
X = int(line[1])

line = input().split()

diff = [abs(int(x)-X) for x in line]

min_ = gcd(diff[0], diff[0])

for df in diff:
    min_ = min(min_, gcd(diff[0], df))

print(min_)
