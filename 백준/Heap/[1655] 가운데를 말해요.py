#https://www.acmicpc.net/problem/1655

import heapq
import sys
N = int(input())
left = []
right = []

for i in range(N):
    v = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left,-v)
    else:
        heapq.heappush(right,v)
    print(left)
    print(right)
    if right and -left[0] > right[0]:
        heapq.heappush(left, -heapq.heappop(right))
        heapq.heappush(right, heapq.heappop(left))
    
    print(-left[0])




#              1

#             1
#          5     

#             1
#          5     2

#             1
#          5     2
#       10

#             -99
#          1       2
#       10   5

#             -99
#          1       2
#       10   5   7

#             -99
#          1       2
#       10   5   7   5

