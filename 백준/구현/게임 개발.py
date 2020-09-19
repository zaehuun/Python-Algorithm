n, m = map(int,input().split())
a,b,head = map(int,input().split())

direct = [0, 1, 2, 3] #북 동 남 서
tmp = [(-1,0),(0,-1),(1,0),(0,1)]
arr = []
visit = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    visit.append([False * m for _ in range(n) ])

visit[a][b] = True

def turn_left(heading):
    heading -= 1
    if heading < 0:
        heading = 3
    return heading
cnt = 0
answer = 1
while True:

    head = turn_left(head)
    dx = tmp[head][0] + a
    dy = tmp[head][1] + b
    

    if arr[dx][dy] == 0 and visit[dx][dy] == False and dx > 0 and dx < n and dy > 0 and dy < m:
        a = dx
        b = dy
        visit[a][b] = True
        answer += 1
        cnt = 0
        continue
    else:
        cnt += 1
    
    if cnt == 4:
        dx = a - tmp[head][0]
        dy = b - tmp[head][1]

        if arr[dx][dy] != 1:
            a = dx
            b = dy
        else:
            break
        cnt = 0
print(answer)
            




