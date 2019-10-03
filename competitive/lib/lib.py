def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

def sieve(n):
    prime = []
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, n+1):
        if is_prime[i]:
            prime.append(i)
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    return prime

