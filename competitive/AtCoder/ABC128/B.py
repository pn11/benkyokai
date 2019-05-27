N = int(input())

S = []
P = []

cities = {}

for i in range(N):
    line = input().split()
    try:
        cities[line[0]].append(i)
    except:
        cities[line[0]] = [i]
    S.append(line[0])
    P.append(int(line[1]))

for k, v in sorted(cities.items()):
    v = sorted(v, key=lambda x: -P[x])
    for vv in v:
        print(vv+1)
