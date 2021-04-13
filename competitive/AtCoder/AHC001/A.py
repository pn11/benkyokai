import math
import numpy as np


def solve():
    n = int(input())
    A = np.zeros(shape=(n, 3), dtype=np.int64)
    recA = np.zeros(shape=(n, 3), dtype=np.int64)

    for i in range(n):
        x, y, r = [int(x) for x in input().split()]
        A[i, 0] = x
        A[i, 1] = y
        A[i, 2] = r

    distances = calc_distances(A)
    for i in range(n):
        min_distance = np.sort(distances[i,:])[1]
        #print(i, min_distance)
        w = math.floor(1.41421356 * min_distance / 2)

        x = A[i, 0]
        y = A[i, 1]
        r = A[i, 2]
        w = min(r, w)
        print(max(x - w//2, 0), max(y-w//2, 0), min(x+w//2, 9999), min(y+w//2, 9999))
        

    #A = A[np.argsort(A[:, 2])]

    #for i in range(n):
        #x, y, r = [A[i, j] for j in range(3)]]
        #for w, h in yield_ratio(area):
        #    rec = rect(x, y, w, h)

def calc_distances(A):
    points = A[:, :2]
    all_diffs = np.expand_dims(points, axis=1) - np.expand_dims(points, axis=0)
    distances = np.sqrt(np.sum(all_diffs ** 2, axis=-1))

    return distances


def yield_ratio(area):
    w = 1
    while True:
        res = area % w
        h = area // w
        if res == 0:
            yield w, h
        # random に増やすとかもあり？
        w += 1
    

def customer_satisfaction(x, y, r, rect):
    if is_inside(x, y, rect):
        s = rec.w*rec.h
        return 1 - (1 - min(r, s) / max(r, s))*(1 - min(r, s) / max(r, s))
    else:
        return 0


def is_inside(x, y, rect):
    xx = x+0.5
    yy = y+0.5
    return rect.x < xx and xx < rect.x + rect.w and rect.y < yy and yy < rect.y+rect.h


def intersects(rect1, rect2):
    return not (rect1.x1 < rect2.x or rect1.x > rect2.x1 or rect1.y1 < rect2.y or rect1.y > rect2.y1)


class rect:
    def __init__(self, x, y, w, h):
        # x,y: bottom_left
        # x1,y1: top_right
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.x1 = x+w
        self.y1 = y+h

def test_is_inside():
    print(is_inside(0, 0, rect(0,0,1,1)))
    print(is_inside(1, 1, rect(0,0,1,1)))

#test_is_inside()
    
solve()
