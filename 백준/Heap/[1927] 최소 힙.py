#https://www.acmicpc.net/problem/1927

import heapq
import sys
N = int(input())
arr = []

for i in range(N):
    v = int(sys.stdin.readline())
    if v == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr,v)

