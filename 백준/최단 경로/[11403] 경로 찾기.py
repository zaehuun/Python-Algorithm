N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] == 0 :
                continue
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1
for i in arr:
    print(' '.join(list(map(str,i))))
