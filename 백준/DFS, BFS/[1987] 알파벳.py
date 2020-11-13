//https://www.acmicpc.net/problem/1987
//백트리킹으로 풀었는데 python으로 제출하면 시간 초과가 떠서 pypy로 제출했다.
//찾아보니 bfs로 풀면 python도 시간 초과 안 뜬다는 말이.. 

import sys
R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]
checked = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]
answer = 0
def dfs(x,y,cnt):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if 0 <= tx < R and 0 <= ty < C and arr[tx][ty] not in checked:
            checked.add(arr[tx][ty])
            dfs(tx,ty,cnt + 1)
            checked.remove(arr[tx][ty])

checked.add(arr[0][0])
dfs(0,0,1)
print(answer)
