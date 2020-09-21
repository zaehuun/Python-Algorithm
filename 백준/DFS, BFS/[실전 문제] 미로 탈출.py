from collections import deque

n, m = map(int,input().split())

arr = [list(map(int,input())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x,y):
    que = deque()
    que.append((x,y,1))
    visit[x][y] = True

    while que:
        x, y, cnt = que.popleft()
        if x == n -1 and y == m - 1:
            return cnt
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx >= n or ty < 0 or ty >= m or arr[tx][ty] == 0 or visit[tx][ty] == True:
                continue
            visit[tx][ty] = True
            que.append((tx,ty,cnt+1))

print(bfs(0,0))
