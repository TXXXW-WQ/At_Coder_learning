# D - Knapsack 1

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

n,w = map(int,input().split())

for _ in range(n):
  