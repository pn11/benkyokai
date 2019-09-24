'''Dの割にはアルゴリズムも実装もかなり簡単？
ABC137 D がぱっと見少し似てるけどこれよりは難しい。'''
N = int(input())
AB = []
for _ in range(N):
  AB.append([int(x) for x in input().split()])

def solve():
  current_time = 0
  for work in sorted(AB, key=lambda x: x[1]):
    current_time += work[0]
    if current_time <= work[1]:
      pass
    else:
      return False
  return True

if solve():
  print('Yes')
else:
  print('No')
