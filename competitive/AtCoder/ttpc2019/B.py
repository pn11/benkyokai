'''正規表現のライブラリを使ってしまうというずるい解法。'''
import re

N = int(input())
prog = re.compile('.*okyo.*ech')

for _ in range(N):
  result = prog.match(input())
  if result:
    print('Yes')
  else:
    print('No')
