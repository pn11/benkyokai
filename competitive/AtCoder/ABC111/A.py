n = input()

ans = ""
for nn in n:
    if nn == "1":
        ans += "9"
    elif nn == "9":
        ans += "1"

print(ans)
