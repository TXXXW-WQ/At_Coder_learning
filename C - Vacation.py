# C - Vacation 

###################################################

import heapq
from heapq import heappop, heappush, heapify
import io
import sys

_INPUT = """\
3
10 40 70
20 50 80
30 60 90

"""
sys.stdin = io.StringIO(_INPUT)

###################################################

n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
for i in range(n):
  a[i],b[i],c[i] = map(int,input().split())
dp = [[0] * 3 for _ in range(n)]
dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]
for i in range(1,n):
  dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + a[i]
  dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + b[i]
  dp[i][2] = max(dp[i-1][1],dp[i-1][0]) + c[i]
print(max(dp[-1]))