line = input().split()
H = int(line[0])
W = int(line[1])

array = []

def get_ij(index):
    i = index // W
    if (i % 2 == 0):
        j = index % W
    else:
        j = W - index % W - 1
    return i+1, j+1


for i in range(H):
    if i % 2 == 0:
        array.extend([int(a) for a in input().split()])
    else:
        array.extend(reversed([int(a) for a in input().split()]))

move_index = []
previous_move = False
for i, a in enumerate(array[:-1]):
    even = a % 2 == 0

    if previous_move and even:
        # print(i, a, 1, previous_move, even)
        move_index.append(i)
        previous_move = True
    elif not previous_move and not even:
        # print(i, a, 2, previous_move, even)
        move_index.append(i)
        previous_move = True
    else:
        previous_move = False

print(len(move_index))

for i in move_index:
    ind_from = get_ij(i)
    ind_to = get_ij(i+1)
    print("{} {} {} {}".format(ind_from[0], ind_from[1], ind_to[0], ind_to[1]))

