'''当時は解けなかったやつに再挑戦。
解法は思いついたけど、実装は結構1時間くらいかかってしまい、コードも汚くなった。
スイッチのオン・オフをビットで表すのが肝なので、
偶奇で分ける部分は問題として蛇足な気がする。
'''
from functools import reduce
import math

N, M = [int(a) for a in input().split()]
s = []
bulb_list = []

for i in range(M):
  line = [int(a) for a in input().split()]
  k = line[0]
  s.append([int(x) for x in line[1:k+1]])
  bulb_list += s[i]

#print(list(set(bulb_list)))
p = [int(a) for a in input().split()]
#print(s)
count = 0

for i in range(int(math.pow(2, N))):
  onoff = format(i, '010b')
  ok = True
  #print('---')
  #print(onoff)
  for j in range(M):
    l = list(map(lambda x: int(onoff[-x]), s[j]))
    mod = reduce(lambda a, b: a+b, l) % 2
    #print(j, s[j], l, p[j], mod)
    if mod != p[j]:
      ok = False
      break
  if ok:
    #print('ok')
    count += 1

print(count)
