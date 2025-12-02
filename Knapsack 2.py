###################################################

import heapq
from heapq import heappop, heappush, heapify
import io
import sys

_INPUT = """\
6 15
6 5
5 6
6 4
6 6
3 5
7 2

"""
sys.stdin = io.StringIO(_INPUT)

###################################################

n,w = map(int, input().split())
dp = [[0] * (w+1) for _ in range(n+1)]
for i in range(1,n):
  wi, vi = map(int, input().split())
  for j in range(w+1):
    if j < wi:
      dp[i+1][j] = dp[i][j]
    else:
      dp[i+1][j] = max(dp[i][j], dp[i][j-wi] + vi)
print(dp[n][w])