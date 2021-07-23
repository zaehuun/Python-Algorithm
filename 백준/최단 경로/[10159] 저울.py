N = int(input())
M = int(input())

arr = [[None] * N for _ in range(N)]

for _ in range(M):
    h, l = map(int,input().split())
    arr[h-1][l-1] = True
    arr[l-1][h-1] = False

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] == None:
                continue

            if arr[i][k] == arr[k][j]:
                arr[i][j] = arr[i][k]
                arr[j][i] = not arr[i][k]
for i in arr:
    print(i.count(None)-1)
