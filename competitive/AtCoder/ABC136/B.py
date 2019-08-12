N = int(input())

if N < 10:
    print(len(range(1, N+1)))
elif N < 100:
    print("9")
elif N < 1000:
    print(str(9 + len(range(100, N+1))))
elif N < 10000:
    print(str(9+900))
elif N < 100000:
    print(str(9+900+len(range(10000, N+1))))
else:
    print("90909")
