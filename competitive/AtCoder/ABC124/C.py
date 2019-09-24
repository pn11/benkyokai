'''0101... か 1010... の2パターンしかないので、両方を計算した。
評価関数は磁性体のエネルギーみたいだったのでenergyという名前に。'''
S = input()
pattern1 = "".join([str(x%2) for x in range(len(S))])
pattern2 = "".join([str((x+1)%2) for x in range(len(S))])

def energy(st1, st2):
  ene = 0
  for i in range(len(st1)):
    ene += abs(int(st1[i])-int(st2[i]))
  return ene

print(min(energy(S, pattern1), energy(S, pattern2)))
