#https://www.acmicpc.net/problem/11286

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
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr,(abs(v),v))

