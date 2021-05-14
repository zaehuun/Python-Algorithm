from collections import deque

N = int(input()) #보드의 크기

K = int(input()) #사과 수

arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(K):
    x,y = map(int,input().split())
    arr[x][y] = 1 #사과 있는 곳 1

L = int(input())
direct_list =["r",'d','l','u']
direct = 0
answer = 0
snake = deque()
snake.append((1,1))
time = 0
control = []

for _ in range(L):
    control.append(input().split())

control_idx = 0

while True:
    nowX, nowY = snake[0]
    if direct == 0:
        nowY = nowY + 1
    elif direct == 1:
        nowX = nowX + 1
    elif direct == 2:
        nowY = nowY - 1
    elif direct == 3:
        nowX = nowX - 1
    if nowX < 1 or nowY < 1 or nowX >= N + 1 or nowY >= N + 1 or (nowX,nowY) in snake: #벽이나 몸에 박음
        answer = answer + 1
        break
    elif arr[nowX][nowY] == 0:
        snake.appendleft((nowX,nowY))
        snake.pop()
    elif arr[nowX][nowY] == 1:
        snake.appendleft((nowX,nowY))
        arr[nowX][nowY] = 0
    answer = answer + 1

    time = time + 1
    if control_idx < len(control):
        if int(control[control_idx][0]) == time:
            if control[control_idx][1] == 'D':
                direct = direct + 1
                if direct > 3:
                    direct = 0
            else:
                direct = direct - 1
                if direct < 0:
                    direct = 3
            control_idx = control_idx + 1
print(answer)

