# A - Triangular Number 

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
ans = 0
for i in range(1,n+1):
  ans+=i
print(ans)