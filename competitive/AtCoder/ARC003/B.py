N = int(input())
s = []
for _ in range(N):
  org = input()
  inv = ""
  for ss in org:
    inv = ss + inv
  s.append((org, inv))
for ss in sorted(s, key=lambda x: x[1]):
  print(ss[0])
