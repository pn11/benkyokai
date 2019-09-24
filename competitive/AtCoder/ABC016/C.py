'''解説読んだら、最短経路を求める方法というのがあった。(ABC012 D らしい。)'''
N, M = [int(x) for x in input().split()]
graph = [[] for _ in range(N+1)]

for _ in range(M):
  A, B = [int(x) for x in input().split()]
  graph[A].append(B)
  graph[B].append(A)

class FriendList:
  def __init__(self, id):
    self.id = id
    self.friends = []
    self.friends_of_friends = []

for i in range(1, N+1):
  foflist = []
  friends = graph[i]
  for friend in friends:
    for fof in graph[friend]:
      def is_friend():
        if fof == i:
          return True
        for fr in friends:
          if fr == fof:
            return True
        return False
      if not is_friend():
        foflist.append(fof)
  print(len(set(foflist)))
