from collections import deque
import copy
import sys
N, M = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
virus = [] #바이러스 위치, 이걸 기반으로 bfs 시작
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i,j))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

answer = 0 #최대 퍼진 바이러스 수
def bfs():
    global answer
    deq = deque(virus)

    resultArr = copy.deepcopy(arr)
    while deq:
        x,y = deq.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < N and -1 < ty < M and resultArr[tx][ty] == 0:
                resultArr[tx][ty] = 2
                deq.append((tx,ty))
    #print(resultArr)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if resultArr[i][j] == 0:
                cnt = cnt + 1
    answer = max(cnt,answer)


def setWalls(cnt):
    if cnt == 3:
        bfs()
    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0 and visit[i][j] == False:
                    arr[i][j] = 1
                    visit[i][j] = True
                    setWalls(cnt + 1)
                    arr[i][j] = 0
                    visit[i][j] = False


setWalls(0)
print(answer)
