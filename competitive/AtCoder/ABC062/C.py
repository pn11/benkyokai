'''Cだと思って油断してかなり苦戦した。
最初に3の倍数のときだけ一列に分解されると思いこんだのが一番の敗因。'''
H, W = [int(x) for x in input().split()]

def solve(H, W):
  if H % 3 == 0 or W % 3 == 0:
    return 0
  else:
    ans = 1e20
    for i in range(max(W//3-1, 1), min(W//3+2, W)):
      a = i
      b = W - a
      for i in range(max(H//2-1, 1), min(H//2+2, H)):
        c = i
        d = H - c
        S = [a*H, b*c, b*d]
        ans = min(ans, max(S)-min(S))
      for i in range(max(b//2-1, 1), min(b//2+2, b)):
        c = i
        d = b - c
        S = [a*H, c*H, d*H]
        ans = min(ans, max(S)-min(S))
  return ans

print(min(solve(H, W), solve(W, H)))
