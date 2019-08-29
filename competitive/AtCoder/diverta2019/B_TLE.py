'''TLE. DPでやれば良さそう？'''

R, G, B, N = [int(a) for a in input().split()]

li = [R, G, B]

li.sort()
count = 0
print(li)

for i in range(N//li[2]+1):
    res = N - li[2] * i
    if res == 0:
        count += 1
        continue
    for j in range(res//li[1]+1):
        res2 = res - li[1] * j
        if res2 == 0:
            count += 1
            continue
        for k in range(res2//li[0]+1):
            if res2 - li[0] * k == 0:
                count += 1
print(count)

