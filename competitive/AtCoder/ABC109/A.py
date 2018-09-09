line = input().split()
A = int(line[0])
B = int(line[1])

if A % 2 == 0 or B % 2 == 0:
    print("No")
else:
    print("Yes")
