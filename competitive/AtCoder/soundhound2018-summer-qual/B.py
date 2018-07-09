line = input()
w = int(input())

out = ""

div = len(line) // w
mod = len(line) % w

for i in range(div):
    out += line[i*w]

if mod != 0:
    out += line[div*w]

print(out)
