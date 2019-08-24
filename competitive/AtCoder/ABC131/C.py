'''A-1までの数を求めてBまでの数から引けばAからBまでになる。'''
a, b, c, d = map(lambda x: int(x), input().split())
a -= 1

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

def calc(ab, c, d):
    return ab - (ab//c + ab//d - ab//lcm(c,d))  

num_a = calc(a, c, d)
num_b = calc(b, c, d)

print(num_b - num_a)
