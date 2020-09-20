n, m = map(int,input().split())

arr = [list(map(int,input())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):

    visit[x][y] = True
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= n or ty < 0 or ty >= m or visit[tx][ty] or arr[tx][ty] == 1:
            continue
        dfs(tx,ty)
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visit[i][j]:
            dfs(i,j)
            answer += 1

print(answer)
