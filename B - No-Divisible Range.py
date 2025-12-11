# B - No-Divisible Range

###################################################

import heapq
from heapq import heappop, heappush, heapify
import io
import sys

_INPUT = """\
5
8 6 10 5 7

"""
sys.stdin = io.StringIO(_INPUT)

###################################################

n = int(input())
a = [int(x) for x in input().split()]
# print(a)
l = 0
r = 0
cou = 0
# ans = []
for i in range(n):
  l = a[i]
  lrsum = l
  for j in range(i+1,n):
    r = a[j]
    lrsum += r
    c = 0
    for s in a[i:j+1]:
      if lrsum % s == 0:
        c = 1
        break
    if not c:
      cou += 1
# print(ans)
print(cou)

