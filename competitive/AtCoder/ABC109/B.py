N = int(input())
used_words = []

pre_word = input()
used_words.append(pre_word)
state = "Yes"


for i in range(N-1):
    W = input()

    if pre_word[-1] != W[0]:
        state = "No"
        break

    for uw in used_words:
        if uw == W:
            state = "No"
            break
    if state == "No":
        break

    used_words.append(W)
    pre_word = W

print(state)
