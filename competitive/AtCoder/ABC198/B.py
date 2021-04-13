N = input()

invN = ""
subN = ""
flag = False

for i in range(len(N)):
    n = N[-(i+1)]
    # print(n)
    if n == '0' and not flag:
        continue
    else:
        flag = True
    invN = invN+n
    subN = n+subN

if subN == invN:
    print('Yes')
else:
    print('No')
