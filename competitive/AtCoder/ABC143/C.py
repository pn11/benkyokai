N = int(input())
S = input()

N2 = N
for i in range(N-1):
    if S[i] == S[i+1]:
        N2 -= 1
print(N2)

    
