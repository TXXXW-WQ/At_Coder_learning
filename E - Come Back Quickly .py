# E - Come Back Quickly
n,m = map(int, input().split())
g = [[] for _ in range(n+1)]
# print(g)
for _ in range(m):
  a,b,c = map(int, input().split())
  a-=1
  b-=1
  g[a].append((b,c))

  for i in range(n):
    dist=[-1]*n
    q=[]
    for j,c in g[i]:
      q.append((j,c))