line = input().split()
N = int(line[0])
K = int(line[1])

if N % K == 0:
    print(0)
else:
    print(1)
