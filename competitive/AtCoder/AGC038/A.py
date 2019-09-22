'''解説読んだ'''
H,W,A,B=[int(x) for x in input().split()]
[print(''.join(["0" if j<A else "1" for j in range(W)])) if i<B else print(''.join(["1" if j<A else "0" for j in range(W)])) for i in range(H)]

# 読みやすいバージョン
for i in range(H):
    if i < B:
        print(''.join(["0" if j < A else "1" for j in range(W)]))
    else:
        print(''.join(["1" if j < A else "0" for j in range(W)]))
