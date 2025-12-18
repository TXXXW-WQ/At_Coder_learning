###################################################

import heapq
from heapq import heappop, heappush, heapify
import io
import sys

_INPUT = """\
8 10
6 5
7 3
6 7
3 4
4 2
3 7
1 3
7 4
6 1
6 1

"""
sys.stdin = io.StringIO(_INPUT)

###################################################

n,m = map(int, input().split())
masu = [[-1] * n for _ in range(n)]
count = 0
# print(masu)
for i in range(m):
  r,c = map(int, input().split())
  r -= 1
  c -= 1
  if r < n-1 and c < n-1:
    if (masu[r][c] == -1) and (masu[r+1][c] == -1) and (masu[r][c+1] == -1) and (masu[r+1][c+1] == -1):
      masu[r][c] = 1
      masu[r+1][c] = 1
      masu[r][c+1] = 1
      masu[r+1][c+1] = 1
      count += 1
    else:
      continue
  else:
    continue

print(masu)
print(count)