A, B = [int(x) for x in input().split()]

s = A+B
if s % 2 == 0:
  print(s//2)
else:
  print('IMPOSSIBLE')
