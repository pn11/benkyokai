S = input()
C_count = 0
C_pos = 0
upper_flag = True
AC_flag = False
if S[0] == 'A':
    for i, c in enumerate(S[2:-1]):
        if c == 'C':
            C_count += 1
            C_pos = i+2
    if C_count == 1:
        for i, c in enumerate(S[1:]):
            if (i+1 != C_pos):
                if c.isupper():
                    upper_flag = False
        if upper_flag:
            print('AC')
            AC_flag = True

if not AC_flag:            
    print('WA')
