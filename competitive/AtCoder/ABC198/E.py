# 書きかけ
N = int(input())
C = [int(x) for x in input().split()]
A = []
B = []
for _ in range(N-1):
    a, b = [int(x) for x in input().split()]
    A.append(a)
    B.append(b)

print(N, C, A, B)


# 1からi までの経路に登場した色
colors = [set()]*N
#colors[0] = C[0]

childs = [list()]*N
for a, b in 

ans = []

def dfs(i, colors):
    if C[i] in colors[i]:
        pass
    else:
        ans.append(i)
        dfs[]


