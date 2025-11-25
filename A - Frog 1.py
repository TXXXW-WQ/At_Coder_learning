# A - Frog 1 

################################

import heapq
from heapq import heappop, heappush, heapify
import io
import sys

_INPUT = """\
6
30 10 60 10 60 50
"""
sys.stdin = io.StringIO(_INPUT)

################################

n = int(input())
h = [int(x) for x in input().split()]
dp = [float('inf')] * n
dp[0] = 0
for i in range(1,n):
  if i <= 1:
    dp[i] = abs(h[i-1] - h[i])
    continue
  dp[i] = min(abs(h[i-1]-h[i])+dp[i-1], abs(h[i-2]-h[i]) + dp[i-2])
print(dp[n-1])
