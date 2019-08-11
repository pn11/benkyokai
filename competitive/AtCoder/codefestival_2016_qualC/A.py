def solve():
    s = input()
    cpos = s.find('C')
    if cpos < 0:
        print('No')
        return
    fpos = s[cpos:].find('F')
    if fpos >= 0:
        print('Yes')
    else:
        print('No')

solve()
