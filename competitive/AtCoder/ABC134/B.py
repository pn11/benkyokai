N, D = [int(x) for x in input().split()]
trees_per_man = 2*D+1
print(N//trees_per_man if N%trees_per_man==0 else N//trees_per_man+1)
