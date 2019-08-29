'''今日の一問。愚直に書いた。負の数の商とあまりは苦手。全部絶対値にしてやったほうが楽。'''
A, B = [int(x) for x in input().split()]

def solve(diff, count):
  if diff <= -10:
    count += abs(diff) // 10
    diff = abs(diff) % 10
  elif diff <= -8:
    count += 1
    diff += 10
  elif diff <= -3:
    count += 1
    diff += 5
  elif diff <= -1:
    count -= diff
    diff = 0
  elif diff == 0:
    print(count)
    return
  elif diff <= 2:
    count += diff
    diff = 0
  elif diff <= 7:
    count += 1
    diff -= 5
  elif diff <= 10:
    count += 1
    diff -= 10
  else:
    count += diff // 10
    diff %= 10
  solve(diff, count)

count = 0
solve(B-A, count)
