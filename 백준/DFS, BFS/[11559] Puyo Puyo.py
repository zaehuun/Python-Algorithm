//https://www.acmicpc.net/problem/11559
//하 fall 함수는 도저히 코드로 생각이 안 나서 가져왔다..
//코드를 보고 나니 이해는 되는데..

from collections import deque
arr = [list(input()) for _ in range(12)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def fall():
    for y in range(6):
        for x in range(11, -1, -1):
            if arr[x][y] == '.': continue
            for k in range(11, x, -1):
                if arr[k][y] == '.':
                    arr[k][y] = arr[x][y]
                    arr[x][y] = '.'


def bfs(x,y):
    visit = set()
    visit.add((x,y))

    deq = deque()
    deq.append((x,y))

    cnt = 1

    pos = []

    while deq:
        a, b = deq.popleft()

        for i in range(4):
            cx = a + dx[i]
            cy = b + dy[i]

            if -1<cx<12 and -1<cy<6 and arr[cx][cy] == arr[x][y] and (cx,cy) not in visit:
                cnt += 1
                visit.add((cx,cy))
                deq.append((cx,cy))
                pos.append((cx,cy))
    if cnt >= 4:
        for i in pos:
            arr[i[0]][i[1]] = '.'
        return True
    return False

answer = 0

while True:
    flag = 0
    for i in range(11, -1, -1):
        for j in range(6):
            if arr[i][j] != '.':
                if bfs(i,j): #4개 이상 있어서 지워진다면
                    flag = 1
              
    fall()
    if flag: answer += 1
    elif flag == 0: break

print(answer)

