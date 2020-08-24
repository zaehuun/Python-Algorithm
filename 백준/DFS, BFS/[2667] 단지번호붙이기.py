//https://www.acmicpc.net/problem/2667


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


n = int(input())
arr = [[int(a) for a in input()] for i in range(n)]
visit = [[False] * n for _ in range(n)]
cnt = 1

def dfs(x, y, cn):
    visit[x][y] = True
    arr[x][y] = cn
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if arr[nx][ny] == 1 and not visit[nx][ny]:

            arr[nx][ny] = cn
            dfs(nx,ny,cn)
            


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visit[i][j]:
            dfs(i,j,cnt)
            cnt += 1
cnt -= 1
count = [0 for i in range(cnt)]

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            count[arr[i][j]-1] += 1
print(cnt)
count.sort()
for i in range(len(count)):
    print(count[i])
