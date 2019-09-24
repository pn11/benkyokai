import queue

INF: int = 1e9
N: int = 10
M: int = 10
maze = [
    "#S######.#",
    "......#..#",
    ".#.##.##.#",
    ".#........",
    "##.##.####",
    "....#....#",
    ".#######.#",
    "....#.....",
    ".####.###.",
    "....#...G#"
]

# スタートの座標
sx = 1
sy = 0

# ゴールの座標
gx = 8
gy = 9

# 移動ベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    que = queue.Queue()
 
    # 各点までの最短距離
    d = [[INF for _ in range(M)] for _ in range(N)]

    que.put((sy, sx))
    d[sy][sx] = 0

    while not que.empty():
        p = que.get()

        # 取り出した状態がゴールなら終了
        if p[0] == gy and p[1] == gx:
            break
        
        for i in range(4):
            # 移動した後の点を(nx, ny)とする
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]

            # 移動が可能かの判定とすでに訪れたことがあるかの判定
            if nx >= 0 and nx < N and ny >= 0 and ny < M and maze[ny][nx] != '#' and d[ny][nx] == INF:
                # 移動できるならキューに入れ、その点の距離をpからの距離+1で確定する
                que.put((ny, nx))
                d[ny][nx] = d[p[0]][p[1]] + 1
    return d[gy][gx]

print(bfs())
