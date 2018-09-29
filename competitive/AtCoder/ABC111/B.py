# 実は9のぞろめより大きい場合はないので繰り上がりが考えなくて良いことに提出時に気づいた。

N = input()
Nint = int(N)

def is_zorome(Nstr):
    init = Nstr[0]
    for n in Nstr[1:]:
        if n != init:
            return False
    return True

def find_min_zorome(Nstr):
    init = Nstr[0]
    candidate = ""
    for _ in range(len(Nstr)):
        candidate += init

    if int(Nstr) < int(candidate):
        return candidate
    else:
        candidate = ""
        if init == "9":
            for _ in range(len(Nstr)+1):
                candidate += "1"
        else:
            for _ in range(len(Nstr)):
                candidate += str(int(init)+1)
        return candidate

if is_zorome(N):
    print(N)
else:
    print(find_min_zorome(N))
