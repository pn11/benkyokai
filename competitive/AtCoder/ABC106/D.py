# TLE

line = input().split()
N = int(line[0])
M = int(line[1])
Q = int(line[2])

L = []
R = []
for i in range(M):
    line = input().split()
    L.append(int(line[0]))
    R.append(int(line[1]))

p = []
q = []
for i in range(Q):
    line = input().split()
    p.append(int(line[0]))
    q.append(int(line[1]))

for pp, qq in zip(p, q):
    count = 0
    for LL, RR in zip(L, R):
        if pp <= LL and RR <= qq:
            count += 1
    print(count)
