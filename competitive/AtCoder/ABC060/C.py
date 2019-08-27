'''ほぼ実装時間のみ。5分くらい？'''
N, T = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]
sum = 0
current = 0

for tt in t:
  if current <= tt:
    current = tt+T
    sum += T
  else:
    diff = current - tt
    current = tt+T
    sum += T - diff
print(sum)
