import math

N = int(input())
S = []

for _ in range(N):
    S.append(input())

def create_hash(_str):
    hash = ""
    for i, a in enumerate(["a", "b", "c", "d", "e",
     "f", "g", "h", "i", "j",
     "k", "l", "m", "n", "o",
     "p", "q", "r", "s", "t",
     "u", "v", "w", "x", "y", "z"]):
        count = 0
        for s in _str:
            if s == a:
                count += 1
        hash += str(count)
    return hash

def combinations(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

hist = {}
for s in S:
    hash = create_hash(s)
    hist[hash] = hist.get(hash, 0) + 1

pairs = 0
for k, v in hist.items():
    if v > 1:
        pairs += combinations(v, 2)
print(pairs)
