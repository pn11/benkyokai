'''蟻本 p.56 のをやってみたが TLE'''
N = int(input())
S = input()
dp = [[0]*5001 for _ in range(5001)]
 
def solve(s1, s2):
  for i in range(len(s1)):
    for j in range(len(s2)):
      if s1[i] == s2[j]:
        dp[i+1][j+1] = dp[i][j] + 1
      else:
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
  return dp[len(s1)][len(s2)]
 
ans = 0
for i in range(1, N):
  ans = max(ans, solve(S[0:i], S[i:]))
print(ans)
