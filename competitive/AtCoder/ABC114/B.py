
S = input()
l = len(S)

min_ = 753

for i in range(l-2):
    number = int(S[i]) * 100 + int(S[i+1])*10 + int(S[i+2])
    min_ = min(abs(number-753), min_)

print(min_)