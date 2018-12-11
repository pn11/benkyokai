N = int(input())

#def height(x, y, h, cx, cz):

def city_dist(x1, y1, x2, y2):
    return(abs(x1-x2)+abs(y1-y2))

def height(x1, y1, cx, cy, H):
    return max(H-city_dist(x1, y1, cx, cy), 0)

x = []
y = []
h = []
non_zero_index = -1

for i in range(N):
    line = [int(a) for a in input().split()]
    x.append(line[0])
    y.append(line[1])
    h.append(line[2])
    if line[2] != 0:
        non_zero_index = i


for cx in range(101):
    for cy in range(101):
        H = h[non_zero_index] + city_dist(x[non_zero_index], y[non_zero_index], cx, cy)
        answer = True
        for i in range(N):
            #print(cx, cy, H, i, x[i], y[i], h[i], height(x[i], y[i], cx, cy, H))
            if h[i] != height(x[i], y[i], cx, cy, H):
                answer = False
                break
        if answer:
            print("{} {} {}".format(cx, cy, H))
            break            
    if answer:
        break
