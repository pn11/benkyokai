'''なんかAからしていつもより難しい気がした。'''
minpos = int(input())

for _ in range(3):
    _ = input()

maxpos = int(input())
k = int(input())

if maxpos - minpos <= k:
    print("Yay!")
else:
    print(":(")
