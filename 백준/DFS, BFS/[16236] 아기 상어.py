//https://inspirit941.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-16236-%EC%95%84%EA%B8%B0-%EC%83%81%EC%96%B4
//도움을 받아서 풀었다
//heapq를 사용하니 좋다

from collections import deque
import heapq

N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int,input().split())))

sx = 0 #상어 위치
sy = 0
size = 2

answer = 0

a = False
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sx = i
            sy = j
            a = True
            break
    if a:
        break

dx = (1,-1,0,0)
dy = (0,0,1,-1)

def bfs(x,y,t):
    check = set()
    check.add((x,y))
    arr[x][y] = 0
    q = deque()
    q.append((x,y,t))

    min_dist = []
    while q:

        x, y, z = q.popleft()
        check.add((x,y))
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            
            if 0 <= tx < N and 0 <= ty < N and (tx,ty) not in check:
                check.add((tx,ty))
                if arr[tx][ty] == 0 or arr[tx][ty] == size:
                    q.append((tx,ty,z+1))
                    continue
                if arr[tx][ty] > size:
                    continue
                else:
                    heapq.heappush(min_dist,(z+1,tx,ty))
    if min_dist:
        return min_dist[0]
    else:
        return None

cnt = 0

while True:
    ret = bfs(sx,sy,0)

    if ret == None:
        break
    
    cnt += 1
    time,sx, sy = ret
        
    if cnt == size:
        size += 1
        cnt = 0
    answer += time

print(answer)



        
