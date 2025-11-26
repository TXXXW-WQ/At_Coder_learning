# B - Frog 2

###################################################

import heapq
from heapq import heappop, heappush, heapify
import io
import sys

_INPUT = """\
2 100
10 10

"""
sys.stdin = io.StringIO(_INPUT)

###################################################

n,k = map(int, input().split())
h = [int(x) for x in input().split()]
# print(h)
inf = float('inf')
dp = [inf] * n
dp[0] = 0
for i in range(1,n):
  best = inf
  start = max(0, i-k)
  for j in range(start,i):
    cost = dp[j] + abs(h[i]-h[j])
    if cost < best:
      best = cost
  dp[i] = best
print(dp[n-1])