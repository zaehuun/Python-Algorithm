//테스트 케이스 잘못보고 이상하게 풀었다. 내일 다시 풀어야지
https://www.acmicpc.net/submit/3055/23840992

from collections import deque
R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

wr = 0
wc = 0

gr = 0
gc = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            wr = i
            wc = j
        elif arr[i][j] == 'S':
            gr = i
            gc = j

def water(i,j):
    checked = [[False] * C for _ in range(R)]
    checked[i][j] = True

    deq = deque()

    deq.append((i,j,0))
    arr[i][j] = 0

    while deq:
        x, y, cnt = deq.popleft()

        for t in range(4):
            tx = x + dx[t]
            ty = y + dy[t]
            if 0<=tx<R and 0<=ty<C and not checked[tx][ty] and arr[tx][ty] =='.':
                arr[tx][ty] = cnt + 1
                deq.append((tx,ty,cnt+1))
                checked[tx][ty] = True

def go(i,j):
    checked = [[False] * C for _ in range(R)]
    checked[i][j] = True

    deq = deque()

    deq.append((i,j,0))
    arr[i][j] = 0

    while deq:
        x, y, cnt = deq.popleft()
        
        for t in range(4):
            tx = x + dx[t]
            ty = y + dy[t]
            
            if 0<=tx<R and 0<=ty<C and not checked[tx][ty]:
                checked[tx][ty] = True
                if arr[tx][ty] == 'D':
                    return cnt+1
                if arr[tx][ty] != 'X' and cnt + 1 < arr[tx][ty]:
                    deq.append((tx,ty,cnt+1))

    return 'KAKTUS'
water(wr,wc)

print(go(gr,gc))
