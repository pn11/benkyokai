N = input()
l = len(N)
N = int(N)

def is753(n):
    if n == 3 or n == 5 or n == 7:
        return 1
    elif n < 3:
        return 0
    elif n < 5:
        return 3
    elif n < 7:
        return 5
    else:
        return 7


def calc_max753(N):
    max753 = ""
    Nstr = str(N)
    for i in range(len(Nstr)-2):
        k = is753(int(Nstr[i])) 
        if  k == 1:
            max753 += str(k) 
            continue
        else:
            max753 += str(k) + calc_max753(pow(10, len(Nstr)-i+1))
            break
    return int(max753)


print(calc_max753(N))