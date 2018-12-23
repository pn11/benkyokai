# 素数を列挙するだけのやつ書いてあきらめた。
import math

N, P = [int(i) for i in input().split()]

def sieve_Eratosthenes(n):
    sq = int(math.sqrt(n))
    is_prime = [True] * sq
    is_prime[0] = False

    p = 2
    while p < sq:
        i = 2
        while i <= sq/p:
            is_prime[p*i-1] = False
            i += 1
        p += 1

    return is_prime

def prime_factorize(n):
    for i in range(2, n+1):
        if n % i == i:
            pass


prime = []
is_prime = sieve_Eratosthenes(10000)
for i, b in enumerate(is_prime):
    if b:
        prime.append(i+1)

print(prime)
