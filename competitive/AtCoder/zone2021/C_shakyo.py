import io
import re
import sys
import numpy as np
_INPUT_ = """\
10
6 7 5 18 2
3 8 1 6 3
7 2 8 7 7
6 3 3 4 7
12 8 9 15 9
9 8 6 1 10
12 9 7 8 2
10 3 17 4 10
3 1 3 19 3
3 14 7 13 1
"""
#sys.stdin = io.StringIO(_INPUT_)


# copied from https://atcoder.jp/contests/zone2021/editorial/1197
# added some comments
# refered https://blog.hamayanhamayan.com/entry/2021/05/01/231111

N = int(input())
A = [tuple(map(int, input().split())) for i in range(N)]

def check(x):
    s = set()
    for a in A:
        # 5つの能力がX以上かどうかを 0b01011 みたいに表わす
        # a[0] >= x だったら 1 を0個左シフトして 0b001
        # a[1] >= x だったら 1 を1個左シフトして 0b010
        # これらを足し合わせる
        s.add(sum(1 << i for i in range(5) if a[i] >= x))
    #print(x, [bin(ss) for ss in s])
    # 3つ選ぶループを回す。圧縮されて set に入っているので、
    # 最大でも 2^5 C 3 通り
    # 全部の bit が1ならそれが最大値。
    for x in s:
        for y in s:
            for z in s:
                if x | y | z == 0b11111:
                    return True
    return False

ok = 0

ng = 10**9 + 1

while ng - ok > 1:
    cen = (ok+ng) //2
    if check(cen):
        ok = cen
    else:
        ng = cen
print(ok)
