'''リアルタイムで解いてたけど、今日の一問だったので解いてみた。
前回解いた方法は覚えてなかったけど、見比べてみるとほぼ同じだった。'''
N = int(input())
x = []
y = []
h = []
nonzero_x = 0
nonzero_y = 0
nonzero_h = 0

for _ in range(N):
    xx, yy, hh = [int(x) for x in input().split()]
    x.append(xx)
    y.append(yy)
    h.append(hh)
    if nonzero_h == 0 and hh != 0:
        nonzero_x = xx
        nonzero_y = yy
        nonzero_h = hh


def solve():
    for cx in range(101):
        for cy in range(101):
            res = True
            calc_h = nonzero_h + abs(nonzero_x-cx) + abs(nonzero_y-cy)
            for i in range(N):
                hh = max(calc_h - abs(x[i]-cx) - abs(y[i]-cy), 0)
                if hh != h[i]:
                    res = False
                    break
            if res:
                print("{} {} {}".format(cx, cy, calc_h))
                return
    return

solve()
