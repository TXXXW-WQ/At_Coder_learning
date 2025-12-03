###################################################

import heapq
from heapq import heappop, heappush, heapify
import io
import sys

_INPUT = """\
3 8
3 30
4 50
5 60

"""
sys.stdin = io.StringIO(_INPUT)

###################################################

n,w = map(int, input().split())
dp = [[0] * (w+1) for _ in range(n+1)]
for i in range(1,n+1):
  wi, vi = map(int, input().split())
  for j in range(w+1):
    if j < wi:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-wi] + vi)
print(dp[n][w])