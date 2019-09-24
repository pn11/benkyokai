import heapq as hq

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
que = []
for i, a in enumerate(A):
    hq.heappush(que, (-a, str(i))) 

for _ in range(M):    
    priority, a = hq.heappop(que)    
    if priority == 0:
        break
    priority = - priority
    priority //= 2
    hq.heappush(que, (-priority, a))

sum_ = 0
for q in que:
    sum_ += q[0]

print(-sum_)
