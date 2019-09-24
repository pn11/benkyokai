S = input()
T = input()

atari = 0

for i in range(3):
    if S[i] == T[i]:
        atari += 1

print(atari)
