'''中心を通るような直線は必ず長方形を半分にする。指定した点が中心と等しくなければ直線は一意に決まる。'''
w, h, x, y = map(lambda x: int(x), input().split())

def is_eq(x, y):
    if abs(x-y) < 1e-9:
        return True
    else:
        return False

if is_eq(w/2, x) and is_eq(h/2, y):
    print("{} 1".format(w*h/2))
else:
    print("{} 0".format(w*h/2))
