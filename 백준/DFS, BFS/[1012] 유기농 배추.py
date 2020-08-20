//https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


loop = int(input())

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

for l in range(loop):

    row, col, bug = map(int,input().split())

    grd = [[0] * col  for _ in range(row)]
    visit = [[False] * col for _ in range(row)]
    for i in range(bug):
        x, y = map(int, input().split())
        grd[x][y] = 1

    cnt = 0

    def dfs(x, y):
        visit[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue
            if visit[nx][ny] or grd[nx][ny] == 0:
                continue

            dfs(nx,ny)




    for i in range(row):
        for j in range(col):

            if not visit[i][j] and grd[i][j] :
                cnt += 1
                dfs(i,j)

    print(cnt)
