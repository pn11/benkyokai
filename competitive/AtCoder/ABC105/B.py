N = int(input())

flag = False
for ic in range(N//4+1):
    for id in range(N//7+1):
        if ic*4+id*7 == N:
            flag = True
            break
    if flag:
        break

if flag == True:
    print("Yes")
else:
    print("No")
