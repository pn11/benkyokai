K = int(input())

mod = K % 2

if mod == 0:
    n_even = K // 2
    n_odd = K // 2 
else:
    n_even = K // 2
    n_odd = K // 2 + 1

print(n_even*n_odd)
