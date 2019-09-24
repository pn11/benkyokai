S = input()

ans = "Yes"
for i, s in enumerate(S):
    if (i+1) %2 == 1:
        if s == 'R' or s == 'U' or s == 'D':
            pass
        else:
            ans = 'No'
            #print(i, s, ans)
            break
    else:
        if s == 'L' or s == 'U' or s == 'D':
            pass
        else:
            ans = 'No'

            break
print(ans)
