'''難しそうに見えたけど、全探索できてしまうので意外と簡単だった。
AtCoder Problems の streak のために急いでたのでコードは汚い。
全探索できない場合だとどう解けば良いのかわからない。
→ 解説を読んで初めて、pi は [1..N] を並び替えたものだと知った。その場合だと
iとpiが等しいかどうかという情報を使うことができる。'''
N = int(input())
p = [int(x) for x in input().split()]

def is_sorted(li):
  for i in range(len(li)-1):
    if li[i] > li[i+1]:
      return False
  return True

ans = is_sorted(p)

def check():
  for i in range(N-1):
    for j in range(i+1, N):
      new = p[:]
      new[j] = p[i]
      new[i] = p[j]
      if is_sorted(new):
        return True
  return False

if ans:
  print("YES")
else:
  if check():
    print("YES")
  else:
    print("NO")
