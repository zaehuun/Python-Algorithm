#https://www.acmicpc.net/problem/2178

from collections import deque

N, M = map(int,input().split())

arr = [list(input()) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

queue = deque([(0,0,1)])
while queue:
    x, y, cnt = queue.popleft()
    if x == N - 1 and y == M - 1:
        print(cnt)
        break
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        
        if -1 < tx < N and -1 < ty < M and arr[tx][ty] == '1':
            arr[tx][ty] = 0
            queue.append((tx,ty,cnt+1))
