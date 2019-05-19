S = input()

s1 = int(S[:2])
s2 = int(S[2:])

def is_month(ss):
    if ss > 0 and ss <= 12:
        return True
    else:
        return False

if is_month(s1) and is_month(s2):
    print('AMBIGUOUS')
elif is_month(s1) and not is_month(s2):
    print('MMYY')
elif is_month(s2) and not is_month(s1):
    print('YYMM')
else:
    print('NA')
