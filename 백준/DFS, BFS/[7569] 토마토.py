#https://www.acmicpc.net/problem/7569
#1년 전에 엄청 어려워했던 문제였는데 신기하다
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
M, N, H = map(int,input().split())
tomato = deque()
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visit = [[[False] * M for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                tomato.append((j,k,i,0))
dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]
answer = 0
while tomato:
    x,y,z,day = tomato.popleft()
    answer = max(day,answer)
    visit[z][x][y] = True
    for i in range(6):
        tx = x + dx[i]
        ty = y + dy[i]
        tz = z + dz[i]
    
        if -1 < tx < N and -1 < ty < M and -1 < tz < H and arr[tz][tx][ty] == 0:
            tomato.append((tx,ty,tz,day+1))
            arr[tz][tx][ty] = 1
def zero_check():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return False
    return True

if zero_check():
    print(answer)
else:
    print(-1)
