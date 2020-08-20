//https://www.acmicpc.net/problem/4963

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


dx = (-1, -1, -1, 0, 1, 1, 1, 0)
dy = (-1, 0, 1, 1, 1, 0, -1, -1)

while True:
    w, h = map(int,input().split())

    if not w:
        break
    lands = [list(map(int,input().split())) for _ in range(h)]


    visit = [[False] * w for _ in range(h)]
    land = 0


    def dfs(x,y):
        visit[x][y] = True

        for i in range(8):
            tx = dx[i] + x
            ty = dy[i] + y

            if tx < 0 or ty < 0 or tx >= h or ty >= w:
                continue
            if not visit[tx][ty] and lands[tx][ty] == 1:
                dfs(tx,ty)


    for i in range(h):
        for j in range(w):
            if lands[i][j] and not visit[i][j]:
                visit[i][j] = True
                land += 1
                dfs(i,j)
    
    print(land)
    



