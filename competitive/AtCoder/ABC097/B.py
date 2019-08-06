'''AtCoder Promblems のおすすめに出てきた。
探索範囲は 1<b<32, 1<p<11 なので、全探索でも間に合う。'''
X = int(input())

max_num = 1
for b in range(2, 32):
    num = b
    for p in range(2, 11):
        num *= b
        if num <= X and num >= max_num:
            max_num = num

print(max_num)
