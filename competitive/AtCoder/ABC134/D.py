'''わからなそうだったので解説を読んで理解して、実装した。
すぐ実装できたけど、答えのフォーマットを間違えて45分悩んだ。
発想の問題で、分かってしまうと簡単だけど、こういうのコンテスト中にできる気がしない。
'''
N = int(input())
a = [0] + [int(x) for x in input().split()]
balls = [0]*(N+1)

for i in range(N, 0, -1):
  if sum([balls[j] for j in range(i, N+1, i)]) % 2 != a[i]:
    balls[i] += 1

ans = []
for i, b in enumerate(balls):
  if b == 1:
    ans.append(i)
print(len(ans))

if len(ans) != 0:
  print(" ".join([str(a) for a in ans]))
