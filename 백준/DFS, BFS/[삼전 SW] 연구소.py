n, m = map(int, input().split())

arr = []
tmp = [[0]* m for i in range(n)]

for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)

result = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y):
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if tx >= 0 and tx < n and ty >= 0 and ty < m:
            if tmp[tx][ty] == 0 :
                tmp[tx][ty] = 2
                dfs(tx,ty)
def check():
    cnt= 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt

def sol(cnt):
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = arr[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    dfs(i,j)
        result.append(check())
        return 
        
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                sol(cnt+1)
                arr[i][j] = 0



sol(0)
print(max(result))
