'''壊れた床で区間を分けて組み合わせを計算することを考えたが、実装がめんどそうだった。計算量もどうなるか分からない。見通し悪そう。
というところまで考えて、解説を見て以下のDPを写経。こんな簡単に書けるのかという感じ。'''
N, M = map(lambda x: int(x), input().split())
a = [int(input()) for _ in range(M)]
mod = 1e9+7

is_broken = [False]*(N+1)
for aa in a:
    is_broken[aa] = True

dp = [0]*(N+1)
dp[0] = 1

for now in range(N):
    for next in range(now+1, min(N, now+2)+1):
        if not is_broken[next]:
            dp[next] += dp[now]
            dp[next] %= mod
print(int(dp[N]))
