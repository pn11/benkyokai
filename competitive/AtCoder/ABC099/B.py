def height(x):
    sum = 0
    for i in range(x):
        sum += i+1
    return sum

line = input().split()
a = int(line[0])
b = int(line[1])

a_pos = b - a - 1
a_height = height(a_pos)

print(a_height - a)
