//https://www.acmicpc.net/problem/2667


from collections import deque

N = int(input())

arr = [list(input()) for _ in range(N)]
check = [[False] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

answer = []
cnt = 0
def bfs(x,y):
    tmp = 1
    check[x][y] = True

    queue = deque()
    queue.append((x,y))

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            tx = cx + dx[i]
            ty = cy + dy[i]

            if -1 < tx < N and -1 < ty < N and arr[tx][ty] == '1' and check[tx][ty] == False:
                check[tx][ty] = True
                queue.append((tx,ty))
                tmp += 1
    answer.append(tmp)

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and check[i][j] == False:
            bfs(i,j)
            cnt += 1
answer.sort()

answer = [cnt] + answer
for i in range(len(answer)):
    print(answer[i])
