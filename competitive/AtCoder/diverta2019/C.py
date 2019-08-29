'''境界条件で間違えまくった'''
import re

N = int(input())
s = [input() for _ in range(N)]

num_end_with_A = 0
num_start_with_B = 0
num_both = 0
num_inner_AB = 0

for ss in s:
    res = re.findall('AB', ss)
    if res:
        num_inner_AB += len(res)
    if ss[0] == 'B' and ss[-1] == 'A':
        num_both += 1
    elif ss[0] == 'B':
        num_start_with_B += 1
    elif ss[-1] == 'A':
        num_end_with_A += 1

if num_end_with_A == 0 and num_start_with_B == 0:
    print(num_inner_AB + max(num_both - 1, 0))
else:
    print(num_inner_AB + min(num_end_with_A, num_start_with_B) + num_both)
