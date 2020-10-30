//https://www.acmicpc.net/problem/2178

from collections import deque
queue = deque()
N, M = map(int, input().split())

arr = [[] for _ in range(N)]
check = [[False] * M for _ in range(N)]

for i in range(N):
    s = input()
    for j in s:
        arr[i].append(int(j))

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def bfs(x,y):
    check[x][y] = True
    arr[x][y] = 1
    queue.append((x,y,1))

    while queue:
        qx, qy, cnt = queue.popleft()
        if qx == N-1 and qy == M-1:
            return cnt
        for i in range(4):
            tx = qx + dx[i]
            ty = qy + dy[i]

            if tx < 0 or tx >= N or ty < 0 or ty >= M or arr[tx][ty] == 0:
                continue
            if check[tx][ty] == True:
                continue
            check[tx][ty] = True
            queue.append((tx,ty,cnt+1))

print(bfs(0,0))

