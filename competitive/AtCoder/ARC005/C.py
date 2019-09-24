'''良い解法が思いつかなかったので解説を読もうとしたけどない。
蟻本の幅優先探索に似たような問題がある。（壁破壊なしの場合。）
../../AntBook/page037.py を参照
道を最初になめて、その後壁を探すので、優先度付きキューを使う。
TLE を繰り返した挙げ句、最終的になんで通ったかよく分からない。
https://atcoder.jp/contests/arc005/submissions?f.Task=&f.Language=&f.Status=&f.User=pn11
コンテスト時間内に解ける気がしない。
'''
import heapq as hq

INF = 1e10
H, W = map(int, input().split())
maze = []
for _ in range(H):
    maze.append(input())

for y in range(H):
    for x in range(W):
        if maze[y][x] == 's':
            sx = x
            sy = y
        elif maze[y][x] == 'g':
            gx = x
            gy = y

# print(sx, sy, gx, gy)

# 移動ベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    que = []

    # スタートから壁を何枚隔てているか
    d = [[INF for _ in range(W)] for _ in range(H)]

    hq.heappush(que, (0, (sy, sx)))
    d[sy][sx] = 0

    while len(que) != 0:
        priority, p = hq.heappop(que)
        if priority >= 3:
            return 100
        #d[p[0]][p[1]] = priority
        # print(priority, p, d[p[0]][p[1]])

        # 取り出した状態がゴールなら終了
        if p[0] == gy and p[1] == gx:
            break
        
        for i in range(4):
            # 移動した後の点を(nx, ny)とする
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]

            # 移動が可能かの判定とすでに訪れたことがあるかの判定
            if nx >= 0 and nx < W and ny >= 0 and ny < H and maze[ny][nx] == '.' and d[ny][nx] == INF:
                # 道に接した道は+壁0枚
                hq.heappush(que, (d[p[0]][p[1]], (ny, nx)))
                d[ny][nx] = d[p[0]][p[1]]
            elif nx >= 0 and nx < W and ny >= 0 and ny < H and maze[ny][nx] == '#' and d[ny][nx] == INF:
                # 壁の場合は+壁1枚
                # 優先度を壁の枚数にするので、同じ壁が複数キューに入っても最短経路から選んでくれる
                hq.heappush(que, (d[p[0]][p[1]] +1, (ny, nx)))
                d[ny][nx] = d[p[0]][p[1]] + 1
            elif  nx >= 0 and nx < W and ny >= 0 and ny < H and maze[ny][nx] == 'g' and d[ny][nx] == INF:
                # ゴールの場合
                hq.heappush(que, (d[p[0]][p[1]], (ny, nx)))
                d[ny][nx] = d[p[0]][p[1]]

    return d[gy][gx]

num_barriers = bfs()

if num_barriers <= 2:
    print('YES')
else:
    print('NO')
