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
for i in range(1,n):
  vi, wi = map(int, input().split())
  for j in range(w+1):
    if j < wi:
      dp[i+1][j] = dp[i][j]
    else:
      dp[i+1][j] = max(dp[i][j], dp[i][j-wi] + vi)
print(dp[n][w])