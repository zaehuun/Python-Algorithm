import sys
import heapq
N, K = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visit= []
#print(arr)
S, X, Y = map(int,sys.stdin.readline().split())

virus = [] #(초,바이러스,x,y) 순으로 heapq에 넣을거임

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            heapq.heappush(virus,(0,arr[i][j],i,j))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

while True:

    if not virus:
        break
    time, v, x, y = heapq.heappop(virus)
    
    if time >= S:
        break

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if -1 < tx < N and -1 < ty < N and arr[tx][ty] == 0:
            arr[tx][ty] = v
            heapq.heappush(virus,(time+1,v,tx,ty))
print(arr[X-1][Y-1])
