//다른 사람이 푼 코드를 보면 뭔 소린지 모르겠다.
//나는 그냥 물 다 흘러보내서 각 지점마다 시간 체크 해놓고 그 다음 고슴도치를 bfs로 돌게 해서 체크 했다.
//https://www.acmicpc.net/submit/3055/23840992

from collections import deque
import copy
R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

gc = 0
gr = 0

water = deque()

wvisited = [[-1] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            wvisited[i][j] = 0
            water.append((i,j))
        elif arr[i][j] == 'S':
            gr, gc = i, j
            visited[i][j] = True
        elif arr[i][j] == 'X':
            wvisited[i][j] = 0
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def flood():
    cnt = 1
    global water
    while water:
        tmp = deque()
        for i in water:
            
            for t in range(4):
                x = i[0] + dx[t]
                y = i[1] + dy[t]

                if -1 < x < R and -1 < y < C and arr[x][y] == '.' and wvisited[x][y] == -1:
                    tmp.append((x,y))
                    wvisited[x][y] = cnt

        water = copy.deepcopy(tmp)
        cnt += 1

def bfs(i,j):
    deq = deque()
    visited[i][j] = True
    
    deq.append((i,j,0))

    while deq:
        x, y, cnt = deq.popleft()

        for t in range(4):
            tx = x + dx[t]
            ty = y + dy[t]

            if -1<tx<R and -1<ty<C and  not visited[tx][ty]:
                visited[tx][ty] = True
                if arr[tx][ty] == 'D':
                    return cnt + 1
                if arr[tx][ty] == '.' and cnt + 1 < wvisited[tx][ty] or wvisited[tx][ty] == -1:
                    deq.append((tx,ty,cnt+1))                        
    return 'KAKTUS'
flood()

print(bfs(gr,gc))
