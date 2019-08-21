''' chokudai 氏の今日の一問より。 https://twitter.com/chokudai/status/1163662673529016321
測ってないけど目標時間ちょうどくらい？ こういう再帰で書けるやつ好き。
'''
N = int(input())

buka = {}
for i in range(N-1):
  b = int(input())
  buka[b] = buka.get(b, []) + [i+2]

def calc(num):
  if len(buka.get(num, [])) > 0:
    salaries = [calc(x) for x in buka[num]]
    salary = max(salaries) + min(salaries) +1
  else:
    salary = 1
  return salary

print(calc(1))
