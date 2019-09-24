'''Z algorithm https://snuke.hatenablog.com/entry/2014/12/03/214243
を参考に実装。PyPy だと間に合うがいくつか WA になる。'''
N = int(input())
S = input()
A = [0]*N

def calc():
  ans = 0
  for l1 in range(N):
    A[0] = 0
    l2 = l1+1
    len_ = 0
    while l2 < N:
      # S[l1:l2] と S[l2:] が何文字目まで等しいか調べる
      while l2+len_< N and l1+len_ < l2 and S[l1+len_] == S[l2+len_]:
        print(len_, S[l1+len_], S[l2+len_])
        len_ += 1

      A[l2] = len_
      if len_ == 0:
        l2 += 1
        continue
      k = 1
      # 既に計算した部分は足す
      while l2+k < N and k+A[k] < len_:
        A[l2+k] = A[k]
        k += 1
      l2 += k
      print(S[l2-k:l2])
      len_ -= k
    print(A)
    ans = max(max(A), ans)
  return ans

print(calc())
