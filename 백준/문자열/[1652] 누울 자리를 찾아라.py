#https://www.acmicpc.net/problem/1652
N = int(input())

arr = [list(input()) for _ in range(N)]

answer = []
def row():
    returnV = 0
    
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == '.':
                cnt += 1
            else: #벽일 때
                if cnt >= 2: #이미 누울 자리가 있을 때
                    returnV += 1
                    cnt = 0
                else: #누울 자리가 없을 때
                    cnt = 0
        if cnt >= 2: returnV += 1

    answer.append(returnV)

def col():
    returnV = 0
    for i in range(N):
        cnt = 0            
        for j in range(N):
            if arr[j][i] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    returnV += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt >= 2: returnV += 1
    answer.append(returnV)

row()
col()
print(answer[0],answer[1])
