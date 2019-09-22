'''ビットでやるやつだと思って張り切って実装したけどTLE'''
import numpy as np
H, W, A, B = [int(x) for x in input().split()]
#for w in range(W):

mat = np.zeros((H, W), np.int8)

def calc(mat):
    ans = True
    for i in range(H):
        s = mat[i,:].sum()
        if s != A and s != H-A:
            ans = False
    for j in range(W):
        s = mat[:,j].sum()
        if s != B and s != H-B:
            ans = False
    return ans

ans = False
for i in range(int(pow(2, H*W))):
    bin_num = format(i, '0{}b'.format(H*W))
    for i in range(H):
        mat[i,:] = [int(i) for i in bin_num[i*W:(i+1)*W]]
    if calc(mat):
        ans = True
        break

if ans:
    for i in range(H):
        print(''.join([str(x) for x in mat[i]]))
else:
    print('No')
