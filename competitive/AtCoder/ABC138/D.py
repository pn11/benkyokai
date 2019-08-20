'''TLE'''
N, Q = [int(a) for a in input().split()]

class Tree:
    def __init__(self):
        self.childs = []
        self.counter = 0

trees = [Tree() for _ in range(N+1)]

a = []
b = []

for _ in range(N-1):
    aa, bb = [int(a) for a in input().split()]
    a.append(aa)
    b.append(bb)
    if aa == 1:
        trees[1].childs.append(bb)
    if bb == 1:
        trees[1].childs.append(aa)



def append_child(tree, parent_id):
    for child in tree.childs:
        for j in range(N-1):
            if a[j] == child:
                if b[j] != parent_id:
                    trees[child].childs.append(b[j])
            if b[j] == child:
                if a[j] != parent_id:
                    trees[child].childs.append(a[j])
        append_child(trees[child], child)

append_child(trees[1], 1)


def count_up(tree, qq):
    tree.counter += qq
    for child in tree.childs:
        count_up(trees[child], qq)

for _ in range(Q):
    pp, qq = [int(a) for a in input().split()]
    count_up(trees[pp], qq)

print(" ".join([str(tree.counter) for tree in trees[1:]]))
