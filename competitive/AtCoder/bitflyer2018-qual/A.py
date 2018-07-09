A = int(input())
B = int(input())

for i in reversed(range(A+1)):
    if i % B == 0:
        print(i)
        break
