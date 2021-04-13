# TLE
from itertools import permutations

def check(S):
    if S[0] == '0':
        return False
    return True

def solve():
    S1 = input()
    S2 = input()
    S3 = input()

    # S1 + S2 = S3
    numlist = [str(i) for i in range(10)]

    se = set()
    for s in S1+S2+S3:
        se.add(s)
    chars = list(se)
    numchar = len(chars)
    if numchar > 10:
        print("UNSOLVABLE")
        return
    for comb in permutations(numlist, numchar):
        # print('=====')
        # print(chars, comb)
        S1R = S1[:]
        S2R = S2[:]
        S3R = S3[:]
        for c, n in zip(chars, comb):
            S1R = S1R.replace(c, n)
            S2R = S2R.replace(c, n)
            S3R = S3R.replace(c, n)
        # print(S1R, S2R, S3R)
        if check(S1R) and check(S2R) and check(S3R):
            lhs = int(S1R) + int(S2R)
            rhs = int(S3R)
            if lhs == rhs:
                print(S1R)
                print(S2R)
                print(S3R)
                return
    print("UNSOLVABLE")

solve()
