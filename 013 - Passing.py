# 013 - Passing（★5）

################################

import heapq
from heapq import heappop, heappush, heapify
import io
import sys

_INPUT = """\
7 9
1 2 2
1 3 3
2 5 2
3 4 1
3 5 4
4 7 5
5 6 1
5 7 6
6 7 3
"""
sys.stdin = io.StringIO(_INPUT)

################################

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))
# print(g)


def dijkstra(s):
    q = []
    dist = [float('inf')] * n
    dist[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        now_cost, now = heapq.heappop(q)
        if now_cost > dist[now]:
            continue
        for to, cost in g[now]:
          if now_cost + cost < dist[to]:
              dist[to] = now_cost + cost
              heapq.heappush(q, (dist[to], to))
    return dist
first = dijkstra(0)
last = dijkstra(n-1)
# print(first)
for i in range(n):
    print(first[i] + last[i])
            
