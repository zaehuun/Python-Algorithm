//https://www.acmicpc.net/problem/14503

N, M = map(int, input().split())

r, c, d = map(int, input().split())
#0 : 북
#1 : 동
#2 : 남
#3 : 서
arr = []

for i in range(N):
    arr.append(list(map(int,input().split())))


cnt = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]
while True:

    if arr[r][c] == 0: #현재 위치 청소
        cnt += 1
        arr[r][c] = 2 
    find = False
    for i in range(4):
        d = d - 1
        if d < 0:
            d = 3
        nx = r + dx[d]
        ny = c + dy[d]
        if arr[nx][ny] == 0:
            r = nx
            c = ny
            find = True
            break
    if find:
        continue
    else:
        r = r - dx[d]
        c = c - dy[d]

        if arr[r][c] == 1:
            break
        
print(cnt)
