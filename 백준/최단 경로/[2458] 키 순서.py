N, M = map(int,input().split())
arr = [[0] * N for _ in range(N)]
for _ in range(M):
    long, short = map(int,input().split())
    arr[long-1][short-1] = 1
    arr[short-1][long-1] = -1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] == 0:
                continue
            if arr[i][k] == arr[k][j]:
                arr[i][j] = arr[i][k]
                arr[j][i] = arr[i][k] * -1
answer = 0
for i in arr:
    if i.count(0) == 1:
        answer += 1
print(answer)
